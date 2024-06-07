import socket
import time

def clientmain():
    # Create a socket object
    clientSock = socket.socket()
    
    # Get the machine hostname (assuming the server is running on the same machine)
    machine = socket.gethostname()
    
    # Define the port number
    port = 389
    
    # Connect to the server
    clientSock.connect((machine, port))
    
    # Prompt the user to enter a message
    message = input("Enter your message: ")
    
    # Continue sending messages until the user types "bye"
    while message.lower().strip() != "bye":
        # Send the message to the server
        clientSock.send(message.encode())
        
        # Receive the response from the server (buffer size is 1024 bytes)
        serverResponse = clientSock.recv(1024).decode()
        
        # Print the sent message and the server's response
        print("Sending message:", message)
        print("Server sent back:", serverResponse)
        
        # Wait for a short period before prompting for the next message
        time.sleep(5)
        
        # Prompt the user to enter another message
        message = input("Enter your message (Type 'bye' to exit): ")
    
    # Close the connection when done
    print("Closing the client side connection..!")
    clientSock.close()

if __name__ == "__main__":
    clientmain()
