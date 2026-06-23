# 1. Sum of Digits
num = 1234
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + digit
    temp = temp // 10

print("Sum of Digits:", sum)


# 2. Reverse a Number
num = 1234
reverse = 0
temp = num

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Reverse Number:", reverse)


# 3. Count Digits in a Number
num = 12345
count = 0
temp = num

while temp > 0:
    count = count + 1
    temp = temp // 10

print("Count Digits:", count)


# 4. Check Even or Odd
num = 17

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 5. Check Prime Number
num = 13
flag = 0

for i in range(2, num):
    if num % i == 0:
        flag = 1

if flag == 0:
    print("Prime")
else:
    print("Not Prime")


# 6. Find Factorial
num = 5
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)


# 7. Find Factors
num = 12

print("Factors:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")


# 8. Check Palindrome Number
num = 121
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


# 9. Check Armstrong Number (Any Power)
num = 153
temp = num
count = 0

while temp > 0:
    count = count + 1
    temp = temp // 10

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10

if num == sum:
    print("Armstrong")
else:
    print("Not Armstrong")


# 10. Find GCD (HCF)
a = 12
b = 18

while b != 0:
    a, b = b, a % b

print("GCD:", a)