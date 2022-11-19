num = int(input("SQRT number: "))
for i in range(0, num):
    if (i ** 2) == num:
        print("YES")
        break
else:
    print("NO")
