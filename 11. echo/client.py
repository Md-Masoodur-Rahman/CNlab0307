import socket

def start_echo_client():
    # Define server address and port
    server_address = ('localhost', 65432)
    
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect(server_address)
    
    try:
        # Input a message from the user
        message = input("Enter a message (type 'shutdown' to stop the server): ")
        
        # Send the message to the server
        client_socket.sendall(message.encode())
        
        # Wait for the response from the server
        data = client_socket.recv(1024)
        print(f'Received from server: {data.decode()}')
    finally:
        # Close the connection
        client_socket.close()

if __name__ == '__main__':
    start_echo_client()
