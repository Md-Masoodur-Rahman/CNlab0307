def get_ip_class(ip_address):
    first_octet = int(ip_address.split('.')[0])
    if first_octet <= 127:
        return 'A'
    elif first_octet <= 191:
        return 'B'
    elif first_octet <= 223:
        return 'C'
    elif first_octet <= 239:
        return 'D (Multicast)'
    else:
        return 'E (Reserved)'

def get_subnet(ip_address):
    ip_class = get_ip_class(ip_address)
    if ip_class == 'A':
        return '255.0.0.0'
    elif ip_class == 'B':
        return '255.255.0.0'
    elif ip_class == 'C':
        return '255.255.255.0'
    else:
        return 'N/A (Class {} has no subnet)'.format(ip_class)

def get_network_id(ip_address):
    ip_class = get_ip_class(ip_address)
    if ip_class == 'A':
        return ip_address.split('.')[0]
    elif ip_class == 'B':
        return '.'.join(ip_address.split('.')[:2])
    elif ip_class == 'C':
        return '.'.join(ip_address.split('.')[:3])
    else:
        return 'N/A (Class {} has no network ID)'.format(ip_class)

def get_host_id(ip_address):
    ip_class = get_ip_class(ip_address)
    if ip_class == 'A':
        return '.'.join(ip_address.split('.')[1:])
    elif ip_class == 'B':
        return '.'.join(ip_address.split('.')[2:])
    elif ip_class == 'C':
        return '.'.join(ip_address.split('.')[3:])
    else:
        return 'N/A (Class {} has no host ID)'.format(ip_class)

def main():
    ip_address = input("Enter an IP address: ")
    ip_class = get_ip_class(ip_address)
    subnet = get_subnet(ip_address)
    network_id = get_network_id(ip_address)
    host_id = get_host_id(ip_address)

    print("IP Class:", ip_class)
    print("Subnet:", subnet)
    print("Network ID:", network_id)
    print("Host ID:", host_id)

if __name__ == "__main__":
    main()
