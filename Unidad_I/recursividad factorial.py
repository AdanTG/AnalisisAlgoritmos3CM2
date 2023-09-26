def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print("Ingrese el valor\n")
valor = input()
valor = int(valor)
print(factorial(valor))