# If two values are same values perform “XOR” operation  
# Perform “XOR” be if two values are same what will be the output. 
#  Perform and operation 1 is even? Or odd? What will the output?  
# Practice all bitwise operator

# Bitwise Operators Practice

a = 5
b = 3

print("Values:", a, b)

# AND operator &
print("AND (&):", a & b)

# OR operator |
print("OR (|):", a | b)

# XOR operator ^
print("XOR (^):", a ^ b)

# NOT operator ~
print("NOT (~a):", ~a)

# Left Shift <<
print("Left Shift (<<):", a << 1)

# Right Shift >>
print("Right Shift (>>):", a >> 1)


# XOR with same values
x = 7
y = 7
print("Same values XOR:", x ^ y)


# Even or Odd using AND
num = 1

if num & 1:
    print(num, "is Odd")
else:
    print(num, "is Even")


# More practice numbers
print("\nMore Practice:")

print("6 & 3 =", 6 & 3)
print("6 | 3 =", 6 | 3)
print("6 ^ 3 =", 6 ^ 3)
print("~5 =", ~5)
print("5 << 2 =", 5 << 2)
print("20 >> 2 =", 20 >> 2)