a, b = 0.1, 3

if a < 0 and b < 0:
    a = abs(a)
    b = abs(b)
elif a < 0 or b < 0:
    a = a + 0.5
    b = b + 0.5
elif a > 0 and b > 0 and a < 0.5 or a > 2 and b < 0.5 or b > 2:
    a = a / 10
    b = b / 10
print(a, b)
