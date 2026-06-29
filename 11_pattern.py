n = int(input("Enter number: "))

# find length of number
length = len(str(n))

temp = n
total = 0


# separate digits
while temp > 0:

    digit = temp % 10

    total = total + (digit ** length)

    temp = temp // 10


# check condition

if total == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")