# INPUT FUNCTION PRACTICE

# 1. Taking string input
name = input("Enter your name: ")
print(name)


# 2. Taking integer input
age = int(input("Enter your age: "))
print(age)


# 3. Taking float input
salary = float(input("Enter salary: "))
print(salary)


# 4. Taking multiple inputs
a, b = input("Enter two numbers: ").split()
print(a, b)


# 5. Convert multiple inputs to int
x, y = map(int, input("Enter two numbers: ").split())
print(x + y)



# OUTPUT FUNCTION PRACTICE

# 6. Simple print
print("Hello Python")


# 7. Print multiple values
name = "John"
age = 20
print(name, age)


# 8. Using separator
print("Python", "Java", "C++", sep="-")


# 9. Using end
print("Hello", end=" ")
print("World")


# 10. Formatting output
marks = 90
print(f"Marks are {marks}")



# ERRORS IN INPUT FUNCTION


# Error 1: int conversion error
age = int(input("Enter age: "))
print(age)

# Input:
# abc

# Error:
# ValueError: invalid literal for int()



# Error 2: float conversion error
num = float(input("Enter number: "))
print(num)

# Input:
# hello

# Error:
# ValueError



# Error 3: not giving required inputs
a, b = input("Enter two values: ").split()
print(a,b)

# Input:
# 10

# Error:
# ValueError: not enough values to unpack



# Error 4: wrong number of values
a,b = map(int,input().split())

# Input:
# 1 2 3

# Error:
# ValueError: too many values to unpack



# Error 5: NameError
# print(value)

# Error:
# NameError: name 'value' is not defined