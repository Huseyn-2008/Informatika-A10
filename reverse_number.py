# HOW TO REVERSE NUMBER
num = 7589
n = num

reversed_num = 0

while num != 0:
    x = num % 10
    reversed_num = reversed_num * 10 + x
    num //= 10
print("Reversed number of", n, "is", reversed_num)
