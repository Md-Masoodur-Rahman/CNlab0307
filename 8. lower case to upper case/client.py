import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name and port
    host = '127.0.0.1'  # The same address as the server
    port = 65432        # The same port as the server

    # Connect to the server
    client_socket.connect((host, port))

    # Input a string from the user
    message = input("Enter a string in lowercase: ")

    # Send the string to the server
    client_socket.send(message.encode())

    # Receive the response from the server
    data = client_socket.recv(1024).decode()
    print(f'Received from server: {data}')

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    start_client()
