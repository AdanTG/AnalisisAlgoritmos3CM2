import random
import time
def mochila_fraccionaria(capacidad, objetos):
    objetos.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_objetos = 0.0
    mochila = []
    for valor, peso in objetos:
        if capacidad >= peso:
            mochila.append((valor, peso))
            total_objetos += valor
            capacidad -= peso
        else:
            fracc = capacidad / peso
            mochila.append((valor * fracc, peso * fracc))
            total_objetos += valor * fracc
            break
    return total_objetos, mochila
resultados = []
for _ in range(10):
    objetos = [(random.randint(1, 50), random.randint(1, 50)) for _ in range(5)]
    capacidad = random.randint(10, 50)
    start_time = time.time()  # Marca el tiempo de inicio
    total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
    end_time = time.time()  # Marca el tiempo de finalización
    tiempo_transcurrido = end_time - start_time  # Calcula el tiempo transcurrido
    resultados.append((objetos, capacidad, total_objetos, mochila, tiempo_transcurrido))
for i, (objetos, capacidad, total_objetos, mochila, tiempo) in enumerate(resultados):
    print(f'Caso {i + 1}:')
    print(f'Objetos: {objetos}')
    print(f'Capacidad de la mochila: {capacidad}')
    print(f'Total de objetos en la mochila: {total_objetos}')
    print(f'Mochila resultante: {mochila}')
    print(f'Tiempo transcurrido: {tiempo} segundos')
    print()