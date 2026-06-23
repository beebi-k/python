# Print given value is positive or not  
# Given char(n) is upper case or lower case(without using built in function) 
#  Pass or fail(have 6subject) eg:s1>35  

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num <0:
    print("Not Positive")
else:
    print("Its Zero")


# Given character is Upper case or Lower case (without built-in function)

ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("Upper Case")
elif ch >= 'a' and ch <= 'z':
    print("Lower Case")
else:
    print("Not an alphabet")


# Pass or Fail (6 subjects, each subject > 35)

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