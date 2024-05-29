import socket
import datetime

SERVER_IP = 'localhost'
SERVER_PORT = 12345
SHUTDOWN_COMMAND = "shutdown"  # Command to shutdown the server

def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((SERVER_IP, SERVER_PORT))
        server_socket.listen(1)
        print("Server started...")

        while True:
            client_socket, client_address = server_socket.accept()
            print("Client connected:", client_address)

            # Receive request from client
            request = client_socket.recv(1024).decode()

            # Check for shutdown command
            if request == SHUTDOWN_COMMAND:
                print("Shutdown command received. Server is shutting down.")
                client_socket.sendall("Server shutting down.".encode())
                client_socket.close()
                break
            else:
                # Generate current date and time
                current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Send response to client
                client_socket.sendall(f"Current date and time: {current_datetime}".encode())

            # Close client socket
            client_socket.close()

    except Exception as e:
        print("Error:", e)

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
