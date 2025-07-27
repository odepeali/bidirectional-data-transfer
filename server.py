import socket
import threading

HOST = '127.0.0.1'  
PORT = 5050         

def handle_client(client_socket, address):
    print(f"[+] Connected to {address}")
    client_socket.send(b"Welcome user! You can chat with the server now.\n")

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            client_msg = data.decode().strip()
            print(f"[{address}] Client says: {client_msg}")

            server_response = input("Server reply: ")
            client_socket.sendall(server_response.encode())

        except ConnectionResetError:
            print(f"[!] Connection lost from {address}")
            break

    print(f"[-] Disconnected from {address}")
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[+] Server running on {HOST}:{PORT}")

    try:
        while True:
            client_socket, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            thread.start()
    except KeyboardInterrupt:
        print("\n[!] Server shutting down.")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
