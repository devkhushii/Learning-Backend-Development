import socket


def server():
    serverSocket=socket.socket()
    machine=socket.gethostname()
    port=389
    serverSocket.bind((machine,port))
    
    serverSocket.listen(5)
    
    print("server is good to go...!!")
    commPipe,address=serverSocket.accept()
    while True:
        
        clientString=commPipe.recv(1024).decode()
       
        if not clientString:
            break
        print(f"Received from client: {clientString} " , str(address))
        
        response=input("enter your response : ")    
       
        print("sending reply to ",str(address))
        commPipe.send(response.encode())
            
       
        
    commPipe.close()
        
if __name__=="__main__" :
    server()