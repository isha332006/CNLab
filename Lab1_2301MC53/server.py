import socket
import random

server_name="Server of Isha Shah" # Creating string with my name
server_int=random.randint(1, 100)

PORT=6000
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost',PORT))
server_socket.listen(1)

print(f"Server listening on port {PORT}...\n")

while True:
    conn,addr=server_socket.accept()
    print(f"Connected by {addr}")

    data=conn.recv(1024).decode() #Recieving Client's message
    if not data:
        conn.close()
        continue

    client_name,client_int=data.split(',')
    client_int=int(client_int)

    if not(1<=client_int<=100): #Terminate if condition not satisfied
        print("Invalid number received, terminating server.")
        conn.close()
        server_socket.close()
        break

    total_sum=client_int+server_int
    print(f"Client's name: {client_name}")
    print(f"Server's name: {server_name}")
    print(f"Client's integer: {client_int}")
    print(f"Server's integer: {server_int}")
    print(f"Sum: {total_sum}\n")

    message=f"{server_name},{server_int}" #Sending reply to client
    conn.sendall(message.encode())

    conn.close()
