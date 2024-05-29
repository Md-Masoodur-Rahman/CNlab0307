def ip_to_binary(ip):
    return ''.join([format(int(x), '08b') for x in ip.split('.')])

def binary_to_ip(binary):
    return '.'.join([str(int(binary[i:i+8], 2)) for i in range(0, 32, 8)])

def get_subnet_ips(ip_address, subnet_mask):
    # Convert IP address to binary
    ip_binary = ip_to_binary(ip_address)
    
    # Number of bits used for the network part
    network_bits = subnet_mask
    
    # Number of bits used for the host part
    host_bits = 32 - network_bits
    
    # Calculate the number of subnets
    num_subnets = 2 ** host_bits
    
    # Calculate the increment in the subnet IDs
    subnet_increment = 2 ** (32 - subnet_mask)
    
    # Generate the subnet addresses
    subnets = []
    for i in range(0, num_subnets, subnet_increment):
        subnet_binary = ip_binary[:network_bits] + format(i, f'0{host_bits}b')
        subnet_ip = binary_to_ip(subnet_binary)
        subnets.append(subnet_ip)
    
    return subnets

def main():
    ip_address = input("Enter the IP address (e.g., 192.168.1.0): ")
    subnet_mask = int(input("Enter the subnet mask (e.g., 28): "))
    
    subnets = get_subnet_ips(ip_address, subnet_mask)
    
    print("Starting network IDs of each subnetwork:")
    for subnet in subnets:
        print(subnet)

if __name__ == "__main__":
    main()
