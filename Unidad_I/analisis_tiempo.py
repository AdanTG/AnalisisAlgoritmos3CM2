import time # Librería para el tiempo

inicio = time.time()
res = 0
for i in range(0, 1000):
    res = res + i
print(res)
fin = time.time()
tiempo_ejecutado = fin - inicio
print(tiempo_ejecutado)