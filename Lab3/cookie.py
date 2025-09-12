import socket
HOST, PORT='',8081
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Raw HTTP Server listening on port {PORT}")
while True:
    client_conn, client_addr=server_socket.accept()
    request=client_conn.recv(1024).decode()
    headers=request.split('\r\n')
    cookie_header=next((h for h in headers if h.startswith('Cookie:')), None)

    if cookie_header is None:
        # First-time visitor, send Set-Cookie
        response=(
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Set-Cookie: sessionid=User123\r\n\r\n"
            "<html><body>Welcome, first-time visitor!</body></html>"
        )
    else:
        # Returning visitor, greet using cookie value
        try:
            sessionid=cookie_header.split('=')[1]
        except IndexError:
            sessionid="Unknown"
        response=(
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n\r\n"
            f"<html><body>Welcome back,{sessionid}!</body></html>"
        )

    client_conn.sendall(response.encode())
    client_conn.close()
