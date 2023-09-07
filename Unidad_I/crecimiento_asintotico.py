import matplotlib.pyplot as plt
import numpy as np

n = np.arange(0, 100)

# Calcular el tiempo de ejecución para cada valor de n
tiempo_constante = np.ones_like(n)
tiempo_logaritmico = np.log2(n)
tiempo_lineal = n
tiempo_n_log_n = n * np.log2(n)
tiempo_cuadratico = n**2

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(n, tiempo_constante, label='O(1)', color='red')
plt.plot(n, tiempo_logaritmico, label='O(log n)', color='green')
plt.plot(n, tiempo_lineal, label='O(n)', color='blue')
plt.plot(n, tiempo_n_log_n, label='O(n log n)', color='purple')
plt.plot(n, tiempo_cuadratico, label='O(n^2)', color='orange')

plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución')
plt.title('Comparación de Órdenes Asintóticos de Análisis')
plt.legend()
plt.grid(True)

plt.ylim(0, max(tiempo_cuadratico))

# Mostrar el gráfico
plt.show()