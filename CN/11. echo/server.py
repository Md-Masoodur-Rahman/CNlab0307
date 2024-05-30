import socket
import threading

def handle_client(connection, client_address):
    try:
        print(f'Connection from {client_address}')
        
        # Receive the data in small chunks and echo it back
        while True:
            data = connection.recv(1024)
            if data:
                if data.decode() == 'shutdown':
                    print('Shutdown command received. Server is shutting down.')
                    return 'shutdown'
                print(f'Received: {data.decode()}')
                connection.sendall(data)
            else:
                break
    finally:
        # Clean up the connection
        connection.close()

def start_echo_server():
    # Define server address and port
    server_address = ('localhost', 65432)
    
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(5)  # Allow up to 5 queued connections
    print(f'Server listening on {server_address}')

    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()
        result = handle_client(connection, client_address)
        if result == 'shutdown':
            break

    print('Closing server socket')
    server_socket.close()

if __name__ == '__main__':
    start_echo_server()
