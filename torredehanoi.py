def torredehanoi(n, a, b, c):
    if n == 1:
        print(f'Mueve el disco 1 de {a} a {b}')
        return
    else:
        torredehanoi(n - 1, a, c, b)
        print(f'Mueve el disco {n} de {a} a {b}')
        torredehanoi(n - 1, c, b, a)

print("Ingrese el número de discos:")
valor = int(input())
torredehanoi(valor, 'A', 'C', 'B')