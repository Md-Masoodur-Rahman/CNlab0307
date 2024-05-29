import socket

SERVER_IP = 'localhost'
SERVER_PORT = 12345
SHUTDOWN_COMMAND = "shutdown"  # Command to shutdown the server

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_PORT))

        # Send request to server
        request = input("Enter 'shutdown' to stop the server or press Enter to get date and time: ")
        if request == SHUTDOWN_COMMAND:
            print("Sending shutdown command to server...")
        else:
            print("Sending request for date and time to server...")
            request = "Request for current date and time"
        client_socket.sendall(request.encode())

        # Receive response from server
        response = client_socket.recv(1024).decode()
        print("Response from server:", response)

    except Exception as e:
        print("Error:", e)

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
