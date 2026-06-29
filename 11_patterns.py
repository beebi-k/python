num = 153

# find length
length = len(str(num))

temp = num
sum = 0


# separate digits
while temp > 0:

    digit = temp % 10

    sum = sum + (digit ** length)

    temp = temp // 10


# check condition

if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")