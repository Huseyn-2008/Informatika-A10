num = int(input("SQRT number: "))
for i in range(0, num):
    if (i ** 2) == num:
        print(f"SQRT of number: {num} is {i}")
        break
else:
    print("NOT FOUND :(")
