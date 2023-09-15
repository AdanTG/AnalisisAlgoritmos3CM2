print("ingrese un numero\n")
num = int(input())
fac=1
for i in range(1, num+1):
    fac *=i
print("el numero factorial de",num, "es>> ",fac)