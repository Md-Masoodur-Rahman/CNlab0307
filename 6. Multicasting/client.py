import socket
import struct

def start_multicast_client():
    multicast_group = '224.1.1.1'
    multicast_port = 10000

    # Create the UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # Allow multiple sockets to use the same PORT number
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to the port that we know will receive multicast data
    sock.bind(('', multicast_port))

    # Tell the operating system to add the socket to the multicast group
    # on all interfaces.
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    try:
        while True:
            print('\nWaiting to receive message')
            data, address = sock.recvfrom(1024)
            print(f'Received {len(data)} bytes from {address}')
            print(f'Data: {data.decode()}')
    except KeyboardInterrupt:
        print('\nClient interrupted and is shutting down.')
    finally:
        print('Closing socket')
        sock.close()

if __name__ == '__main__':
    start_multicast_client()
