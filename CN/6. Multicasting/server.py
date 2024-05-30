import socket
import struct
import time

def start_multicast_server():
    multicast_group = '224.1.1.1'
    multicast_port = 10000

    # Create the UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # Set the time-to-live for messages to 1 to ensure the messages do not go past the local network segment
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    try:
        while True:
            message = 'Hello, Multicast Group!'
            print(f'Sending: {message}')
            sent = sock.sendto(message.encode(), (multicast_group, multicast_port))

            time.sleep(5)
    except KeyboardInterrupt:
        print('\nServer interrupted and is shutting down.')
    finally:
        print('Closing socket')
        sock.close()

if __name__ == '__main__':
    start_multicast_server()
