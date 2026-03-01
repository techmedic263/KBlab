def is_valid_part(part):

    if not part.isdigit():
        return False

    if len(part) > 1 and part[0] == '0':
        return False

    value = int(part)
    if 0 <= value <= 255:
        return True

    return False
print(is_valid_part("255"))  # True
print(is_valid_part("256"))  # False
print(is_valid_part("01"))   # False
print(is_valid_part("0"))    # True

# Task 2

def is_valid_ip(ip):

    parts = ip.split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if not is_valid_part(part):
            return False

    return True
print("######################")
print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False

# Part 2

def decimal_to_binary(n):
    if n == 0:
        return "0"

    if n == 1:
        return "1"

    return decimal_to_binary(n // 2) + str(n % 2)

# Test cases
print(decimal_to_binary(10))   # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1))    # "1"
print('###############################')

# Task 2

def binary_to_decimal(b):
    if b == "":
        return 0

    leftmost = int(b[0])
    remaining = b[1:]

    return leftmost * (2 ** (len(b) - 1)) + binary_to_decimal(remaining)
print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1
print('###############')

# Part 3

def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return "Invalid IP address"

    parts = ip.split('.')

    binary_parts = []
    for part in parts:
        binary_part = decimal_to_binary(int(part))
        binary_parts.append(binary_part)

    return '.'.join(binary_parts)

print(ip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"))  # "Invalid IP address"



# i thought we where gonna start converting Hexidecmial and IP adress lol!!!!!!!!