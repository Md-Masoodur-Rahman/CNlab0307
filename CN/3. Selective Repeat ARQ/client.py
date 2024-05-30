import socket

SERVER_IP = 'localhost'
SERVER_PORT = 12346  # Change the port number
WINDOW_SIZE = 4  # Selective Repeat window size
SHUTDOWN_MESSAGE = "shutdown"  # Shutdown message

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter message to send (type 'shutdown' to stop the server): ")

        # Send message to the server
        client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

        # Check for shutdown message
        if message == SHUTDOWN_MESSAGE:
            print("Shutdown command sent. Waiting for server response...")
            break

        # Receive acknowledgment
        ack_data, _ = client_socket.recvfrom(1024)
        ack_message = ack_data.decode()
        print("ACK received:", ack_message)

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    main()
