def fibonacci(n):
  num1 = 0
  num2 = 1

  fio = [num1, num2]

  for i in range(2, n):
    num3 = num1 + num2
    fio.append(num3)
    num1 = num2
    num2 = num3

  return fio

print("Ingrese el valor\n>>",end="")
valor = input()
valor = int(valor)
print(fibonacci(valor))