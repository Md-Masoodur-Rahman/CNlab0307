import socket

def get_local_ip():
    # Get the local hostname
    hostname = socket.gethostname()
    
    # Get the IP address of the local machine
    ip_address = socket.gethostbyname(hostname)
    
    return ip_address

def get_remote_ip(remote_host):
    try:
        # Get the IP address of a remote machine
        ip_address = socket.gethostbyname(remote_host)
        return ip_address
    except socket.error as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Local Machine IP Address:", get_local_ip())
    
    remote_host = input("Enter the hostname or IP address of the remote machine: ")
    print("Remote Machine IP Address:", get_remote_ip(remote_host))
