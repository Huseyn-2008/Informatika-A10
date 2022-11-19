x = '1357'
y = list(x)
z = 0
for i in y:
    if int(i) % 2 == 0:
        z = i
if z in y:
    y.remove(z)
    for i in y:
        print(i, end="")
else:
    print(x)
