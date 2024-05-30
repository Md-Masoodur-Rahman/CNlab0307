import socket
import time

SERVER_IP = 'localhost'
SERVER_PORT = 12346  # Change the port number
WINDOW_SIZE = 4  # Selective Repeat window size
SHUTDOWN_MESSAGE = "shutdown"  # Shutdown message

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    print("Server started...")

    while True:
        receive_data, client_address = server_socket.recvfrom(1024)
        sentence = receive_data.decode()
        print("Received:", sentence)

        # Check for shutdown message
        if sentence == SHUTDOWN_MESSAGE:
            print("Shutdown command received. Server is shutting down.")
            break

        # Simulate processing delay
        time.sleep(1)

        # Send acknowledgment
        server_socket.sendto(b'ACK', client_address)

    # Close the server socket
    server_socket.close()

if __name__ == "__main__":
    main()
