import ipaddress

def list_subnet_addresses(ip_str, subnet_mask):
    # Create an IP network object for the given subnet
    network = ipaddress.IPv4Network(f"{ip_str}/{subnet_mask}", strict=False)
    
    # Determine the size of each subnet
    subnet_size = 32 - subnet_mask
    increment = 2 ** subnet_size

    # List to store the network addresses of each subnet
    subnet_list = []

    # Generate all subnets
    for i in range(0, 2**(32 - network.prefixlen), increment):
        subnet = ipaddress.IPv4Address(int(network.network_address) + i)
        subnet_list.append(subnet)
    
    return subnet_list

def main():
    # Get input from the user
    ip_str = input("Enter the IP address (e.g., 192.168.1.0): ")
    subnet_mask = input("Enter the subnet mask (e.g., 28): ")

    try:
        subnet_mask = int(subnet_mask)
        # Validate subnet mask
        if not (0 <= subnet_mask <= 32):
            raise ValueError("Subnet mask must be between 0 and 32")
        
        # Get list of subnet addresses
        subnet_addresses = list_subnet_addresses(ip_str, subnet_mask)
        
        # Print the results
        print("Starting network IDs of each subnetwork:")
        for addr in subnet_addresses:
            print(addr)
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
