import socket

def server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', port))

    print("Server is running...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received message from client: {data.decode()}")

        # Echo back to the client
        server_socket.sendto(data, client_address)

    server_socket.close()

if __name__ == "__main__":
    server(9999)
