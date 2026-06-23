# 1. int to float
a = 10
print(float(a), type(float(a)))

# 2. int to str
print(str(a), type(str(a)))

# 3. int to bool
print(bool(a), type(bool(a)))


# 4. float to int
b = 10.5
print(int(b), type(int(b)))

# 5. float to str
print(str(b), type(str(b)))

# 6. float to bool
print(bool(b), type(bool(b)))


# 7. str to int
c = "100"
print(int(c), type(int(c)))

# 8. str to float
d = "10.5"
print(float(d), type(float(d)))

# 9. str to bool
e = "True"
print(bool(e), type(bool(e)))


# 10. bool to int
x = True
print(int(x), type(int(x)))

# 11. bool to float
print(float(x), type(float(x)))

# 12. bool to str
print(str(x), type(str(x)))


# 13. int(0) to bool
print(bool(0), type(bool(0)))

# 14. int(1) to bool
print(bool(1), type(bool(1)))


# 15. float(0.0) to bool
print(bool(0.0), type(bool(0.0)))

# 16. float(1.5) to bool
print(bool(1.5), type(bool(1.5)))


# 17. empty string to bool
print(bool(""), type(bool("")))

# 18. non-empty string to bool
print(bool("Python"), type(bool("Python")))


# 19. negative int to float
print(float(-5), type(float(-5)))

# 20. negative float to int
print(int(-5.8), type(int(-5.8)))


# 21. string number to int
print(int("50"), type(int("50")))

# 22. string number to float
print(float("50.25"), type(float("50.25")))


# 23. bool False to int
print(int(False), type(int(False)))

# 24. bool True to float
print(float(True), type(float(True)))

# Error 1: letters cannot convert to int
print(int("abc"))

# Error 2: decimal string cannot convert directly to int
print(int("10.5"))

# Error 3: invalid float conversion
print(float("hello"))