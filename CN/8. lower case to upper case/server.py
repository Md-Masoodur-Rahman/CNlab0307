import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name and port
    host = '127.0.0.1'  # Localhost
    port = 65432        # Port to listen on

    # Bind the socket to the port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f'Server listening on {host}:{port}')

    # Accept a connection
    client_socket, addr = server_socket.accept()
    print(f'Connection from {addr}')

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print(f'Received from client: {data}')

    # Convert to uppercase
    upper_case_data = data.upper()

    # Send the converted data back to the client
    client_socket.send(upper_case_data.encode())

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    start_server()
