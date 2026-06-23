# 1. Sum of Digits
num = int(input("Enter number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit
    temp = temp // 10

print("Sum of digits:", sum)



# 2. Reverse a Number
num = int(input("Enter number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Reverse:", reverse)



# 3. Count Digits in a Number
num = int(input("Enter number: "))
count = 0
temp = num

while temp > 0:
    count = count + 1
    temp = temp // 10

print("Count of digits:", count)



# 4. Check Even or Odd
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")



# 5. Check Prime Number
num = int(input("Enter number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")



# 6. Factorial of a Number
num = int(input("Enter number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)



# 7. Find Factors of a Number
num = int(input("Enter number: "))

print("Factors:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")



# 8. Check Palindrome Number
num = int(input("Enter number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if num == reverse:
    print("\nPalindrome")
else:
    print("\nNot Palindrome")



# 9. # Armstrong Number with any power

num = int(input("Enter number: "))

temp = num
count = 0

# Count number of digits
while temp > 0:
    count = count + 1
    temp = temp // 10


temp = num
sum = 0

# Calculate Armstrong value
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10


if num == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")



# 10. Find GCD (HCF) of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD (HCF):", a)