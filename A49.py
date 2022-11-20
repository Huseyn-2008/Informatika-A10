x = int(input("3 reqemli eded: "))
a = (x // 100) % 10
b = (x // 10) % 10
c = x % 10
y = []

if a > b and a > c:
    y.append(a)
if b > a and b > c:
    y.append(b)
if c > a and c > b:
    y.append(c)

if a < b and a > c:
    y.append(a)
if b > a and b < c:
    y.append(b)
if c < a and c > b:
    y.append(c)

if a < b and a < c:
    y.append(a)
if b < a and b < c:
    y.append(b)
if c < a and c < b:
    y.append(c)

if a == b and a == c and b == c:
    y.append(a)
    y.append(b)
    y.append(c)

for i in y:
    print(i, end="")
