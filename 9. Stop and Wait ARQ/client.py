import socket

def client(port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("Enter message to send: ")

    # Send the message to the server
    client_socket.sendto(message.encode(), ('localhost', port))

    # Receive response from server
    response, server_address = client_socket.recvfrom(1024)
    print(f"Received response from server: {response.decode()}")

    client_socket.close()

if __name__ == "__main__":
    client(9999)
