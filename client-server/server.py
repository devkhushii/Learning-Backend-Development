import socket

def server():
    # Create a new socket object using the default constructor
    serverSocket = socket.socket()
    
    # Get the hostname of the machine where the server is running
    machine = socket.gethostname()
    
    # Define the port number on which the server will listen for connections
    port = 389
    
    # Bind the socket to the specified machine and port
    serverSocket.bind((machine, port))
    
    # Set the server socket to listen for incoming connections
    # The parameter 5 specifies the maximum number of queued connections
    serverSocket.listen(5)
    
    print("Server is good to go...!!")
    
    # Accept a connection from a client
    commPipe, address = serverSocket.accept()
    
    # Start an infinite loop to keep the server running and handling client messages
    while True:
        # Receive data from the client
        # The buffer size is 1024 bytes
        clientString = commPipe.recv(1024).decode()
        
        # If no data is received, break the loop (client has disconnected)
        if not clientString:
            break
        
        # Print the message received from the client along with the client's address
        print(f"Received from client: {clientString}", str(address))
        
        # Prompt the server user to enter a response
        response = input("Enter your response: ")
        
        # Print a message indicating that the response is being sent to the client
        print("Sending reply to", str(address))
        
        # Send the response to the client
        commPipe.send(response.encode())
    
    # Close the communication pipe (connection) with the client
    commPipe.close()

if __name__ == "__main__":
    server()

