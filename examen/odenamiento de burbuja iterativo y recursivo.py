a = 0
while a < 5:
    print("Selecciona el modo de busqueda de burbuja:")
    print("1. interativa")
    print("2. recursiva")

    opcion = input("Ingrese el número del ordenamiento deseado: ")
   
    lista = [5, 3, 8, 4, 6]
    
    if opcion == '1':
        # Ordenar la lista de forma iterativa usando el algoritmo de burbuja
        for i in range(len(lista)):
            for j in range(len(lista) - i - 1):
               if lista[j] > lista[j+1]:
                   temp = lista[j]
                   lista[j] = lista[j+1]
                   lista[j+1] = temp
        print("Lista ordenada de forma iterativa:", lista)
    
    elif opcion == '2':
        # Definir una función recursiva para ordenar la lista usando el algoritmo de burbuja
        def listarecursiva(lista, n):
            if n <= 1:
                return
            for i in range(n - 1):
                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
            listarecursiva(lista, n-1)
        
        # Llamar a la función recursiva para ordenar la lista
        listarecursiva(lista, len(lista))
        print("Lista ordenada de forma recursiva:", lista)