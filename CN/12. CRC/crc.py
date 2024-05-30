def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0: pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    checkword = tmp
    return checkword

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    print("CRC is : ", remainder)
    return codeword

def decodeData(data, key):
    remainder = mod2div(data, key)
    return remainder

def main():
    data = input("Enter data bits: ")
    key = input("Enter CRC key: ")
    
    encoded_data = encodeData(data, key)
    print("Encoded data (with CRC):", encoded_data)
    
    received_data = input("Enter received data bits: ")
    
    remainder = decodeData(received_data, key)
    if '1' in remainder:
        print("Error detected: Yes")
    else:
        print("Error detected: No")

if __name__ == "__main__":
    main()
