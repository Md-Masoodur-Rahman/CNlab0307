# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def ip_to_binary(ip_address):
    # If the input is already in binary format, return it directly
    if '.' not in ip_address:
        return ip_address
    
    # Split the IP address into octets
    octets = ip_address.split('.')
    
    # Convert each octet to binary and join them together
    binary_ip = ''.join([bin(int(octet))[2:].zfill(8) for octet in octets])
    
    return binary_ip
def binary_to_dotted_decimal(binary_ip):
    # Split the binary IP address into octets
    octets = [binary_ip[i:i+8] for i in range(0, len(binary_ip), 8)]
    
    # Convert each octet to decimal and join them with dots
    decimal_ip = '.'.join([str(int(octet, 2)) for octet in octets])
    
    return decimal_ip
def findClass(ip):
    try:
        ip=ip.split(".")
        ip=[int(i) for i in ip]
        if ip[0] >=0 and ip[0] <= 127:
            return "A"
        elif ip[0] >=128 and ip[0] <= 191:
            return "B"
        elif ip[0] >= 192 and ip[0] <= 223:
            return "C"
        elif ip[0] >= 224 and ip[0] <= 239:
            return "D"
        else:
            return "E"

    except:
        return "Invalid IP Address format"
def sep(ip,className):
        if className == "A":
            print("Network ID :",ip[0],)
            print("Host ID :",".".join(ip[1:4]))
        elif className == "B":
            print("Network ID :",".".join(ip[0:2]))
            print("Host ID :",".".join(ip[2:4]))
        elif className == "C":
            print("Network ID :",".".join(ip[0:3]))
            print("Host ID :",ip[3])
        elif className == "D":
            print("Network ID :",".".join(ip[0:4]))
        else:
            print("In this class,IP Address can't divide into network/Host Address")
            

#Driver Code
#Driver Code
ip=input("Enter IP Address(Classful):")

if '.' in ip:
    networkClass=findClass(ip)
    print("Given IP Address belongs to Class:",networkClass)
    ip=ip.split(".")
    sep(ip,networkClass)
else:
    ip = binary_to_dotted_decimal(ip)
    print(ip)
    network_class = findClass(ip)
    print("IP Address Class:", network_class)
    ip = ip.split(".")
    sep(ip, network_class)