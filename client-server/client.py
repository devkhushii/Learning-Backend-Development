import socket
import time

def clientmain():
    clientSock=socket.socket()
    machine=socket.gethostname()
    port=389
    
    clientSock.connect((machine,port))
    
    message=input("Enter your message :")
    
    while message.lower().strip() != "bye":
       
        clientSock.send(message.encode())
        serverResponse=clientSock.recv(1024).decode()
        print("sending message ", message)
        print("server sent back ",serverResponse)
        time.sleep(5)
        message = input("Enter your message (Type 'bye' to exit): ")
    
    print("closing the client side connnection..!")
    clientSock.close()
    

if __name__=="__main__" :
    clientmain( )