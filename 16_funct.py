def add(a, b):
    return a + b

print("adding",add(10, 20))

def square(n):
    return n * n

print("square",square(6))

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(9))

def largest(a, b):
    if a > b:
        return a
    return b

print(largest(15, 8))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(13))

def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch in vowels:
            count += 1

    return count

print(count_vowels("Programming"))


def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(list_sum([10, 20, 30, 40]))


def find_max(numbers):
    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum

print(find_max([12, 45, 7, 89, 23]))