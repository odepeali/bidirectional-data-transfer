import socket

host = '127.0.0.1'  
port = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host, port))
    print(client.recv(1024).decode()) 
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        client.sendall(msg.encode())
        reply = client.recv(1024)
        print("Server:", reply.decode())
