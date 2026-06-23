print("1. Arithmetic Operators")
# Operators: + - * / % // **

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

print("2. Comparison Operators")
# Operators: == != > < >= <=

x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print ("3. Assignment Operators")
# Operators: = += -= *= /= %=

a = 10

a += 5
print(a)

a -= 3
print(a)

a *= 2
print(a)

a /= 4
print(a)

a %= 3
print(a)

print("4. Logical Operators")
# Operators: and or not

age = 20

print(age > 18 and age < 30)
print(age < 18 or age == 20)
print(not(age > 18))

print("5. Identity Operators")
# Operators: is is not

a = [1,2,3]
b = a
c = [1,2,3]

print(a is b)
print(a is c)
print(a is not c)

print("6. Membership Operators")
# Operators: in not in

name = "Python"

print("P" in name)
print("z" in name)
print("x" not in name)

print("7. Bitwise Operators")
# Operators: & | ^ ~ << >>

a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)