# len(n) must be == 5

n = "12345"

m = list(n)

m.sort()

x = set(m)
x1 = list(x)
x1.sort()

if x1 == m:
    print("REQEMLER EYNIDIR")
if x1 != m:
    print("REQEMLER AYRIDIR")
print(m,x1)
