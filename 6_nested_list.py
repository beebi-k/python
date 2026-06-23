# # Convert Binary to Decimal

# binary = input("Enter binary number: ")

# decimal = 0
# power = 0

# for i in binary[::-1]:
#     decimal = decimal + int(i) * (2 ** power)
#     power = power + 1

# print("Decimal value:", decimal)


# # Binary to Decimal conversion

# binary = input("Enter binary number: ")

# decimal = int(binary, 2)

# print("Decimal value:", decimal)

# Binary to Decimal conversion

binary = input("Enter binary number: ")

decimal = 0
base = 1

i = len(binary) - 1

while i >= 0:
    digit = int(binary[i])
    
    decimal = decimal + (digit * base)
    
    base = base * 2
    
    i = i - 1

print("Decimal value:", decimal)