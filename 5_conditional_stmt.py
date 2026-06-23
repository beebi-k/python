# 1. Check given value is positive or not

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
else:
    print("Not Positive")


# 2. Check character is Upper case or Lower case
# Without using built-in functions

ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("Upper Case")
elif ch >= 'a' and ch <= 'z':
    print("Lower Case")
else:
    print("Not an alphabet")


# 3. Pass or Fail (6 subjects)

s1 = int(input("Enter subject 1 marks: "))
s2 = int(input("Enter subject 2 marks: "))
s3 = int(input("Enter subject 3 marks: "))
s4 = int(input("Enter subject 4 marks: "))
s5 = int(input("Enter subject 5 marks: "))
s6 = int(input("Enter subject 6 marks: "))


if s1 > 35 and s2 > 35 and s3 > 35 and s4 > 35 and s5 > 35 and s6 > 35:
    print("Pass")
else:
    print("Fail")