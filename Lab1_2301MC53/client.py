import socket

client_name="Client of Isha Shah"
while True:
    try:
        client_int=int(input("Enter a number between 1 and 100 for client: "))
        if 1<=client_int<=100:
            break
        else:
            print("Number must be between 1 and 100.")
    except ValueError:
        print("Invalid number. Try again.")

PORT=6000
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('localhost',PORT)) #Connect to server

message=f"{client_name},{client_int}"
client_socket.sendall(message.encode())

data=client_socket.recv(1024).decode() #Recieving Server's reply
server_name,server_int=data.split(',')
server_int=int(server_int)

total_sum = client_int+server_int
print(f"Client's name: {client_name}")
print(f"Server's name: {server_name}")
print(f"Client's integer: {client_int}")
print(f"Server's integer: {server_int}")
print(f"Sum: {total_sum}\n")

client_socket.close() #Close socket
