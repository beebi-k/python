# 1. Observe (Understanding Loops)

# A loop is used to execute a block of code repeatedly until a condition is satisfied.

# Types of loops:
# for loop
# while loop
# 2. for Loop

# Used when we know how many times we want to repeat.

# Syntax:
# for variable in sequence:
#     statements

# Example:

# for i in range(1,6):
#     print(i)

# Output:

# 1
# 2
# 3
# 4
# 5
# 3. while Loop

# Used when the number of iterations is not fixed.

# Syntax:
# while condition:
#     statements

# Example:

# i = 1

# while i <= 5:
#     print(i)
#     i = i + 1

# Output:

# 1
# 2
# 3
# 4
# 5
# 4. Loop Control Statements
# break

# Stops the loop completely.

# Example:

# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)

# Output:

# 1
# 2
# 3
# 4
# continue

# Skips current iteration.

# Example:

# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)

# Output:

# 1
# 2
# 4
# 5
# pass

# Does nothing (placeholder).

# Example:

# for i in range(5):
#     pass
# 5. Nested Loop

# Loop inside another loop.

# Example:

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

# Output:

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        while n % 2 == 0:
            n = n // 2

        return n == 1
    
class Solution:
    def isPowerOfThree(self, n):

        if n <= 0:
            return False

        while n % 3 == 0:
            n = n // 3

        return n == 1