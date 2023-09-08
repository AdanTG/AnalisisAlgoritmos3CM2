import math

i = 0
while i<5:
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. todas")
    opcion = input("Ingrese el número de la operación deseada: ")

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = num1 + num2
        print("Resultado:", resultado)
    elif opcion == '2':
        resultado = num1 - num2
        print("Resultado:", resultado)
    elif opcion == '3':
        resultado = num1 * num2
        print("Resultado:", resultado)
    elif opcion == '4':
        resultado = num1 / num2
        print("Resultado:", resultado)
    elif opcion == '5':
        resultado = num1 + num2
        print("Resultado:", resultado)

        resultado = num1 - num2
        print("Resultado:", resultado)

        resultado = num1 * num2
        print("Resultado:", resultado)

        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Opción no válida")