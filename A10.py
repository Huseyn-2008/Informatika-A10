num = int(input("Num: "))

num1 = abs(num)

x = (num1 // 10) // 10
y = (num1 // 10) % 10
z = num1 % 10

toplama = x + y + z
vurma = x * y * z
if num < 0:  
    toplama = -toplama
    vurma = -vurma
    
print(toplama,vurma)
