digits = [0,9]

for i in range(len(digits) - 1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        break
    else:
        digits[i] = 0
else:
    digits = [1] + digits

print(digits)