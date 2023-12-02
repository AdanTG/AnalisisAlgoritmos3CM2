import time

class Graph:
    def __init__(self):
        # Conjunto de vertices
        self.nodes = set()
        # conjunto de aristas
        self.edges = {}

    def add_vertex(self, valor):
        # Agregar un nuevo vértice al grafo
        self.nodes.add(valor)
        # Inicializar la lista de aristas para el vértice agregado
        self.edges[valor] = []

    def add_edge(self, devertice, avertice, peso):
        # Agregar una nueva arista al grafo
        self.edges[devertice].append((avertice, peso))
        self.edges[avertice].append((devertice, peso))

def dijkstra(graph, start):
    # Inicializar distancias y padres
    distancia = {node: float('infinity') for node in graph.nodes}
    distancia[start] = 0
    padre = {node: None for node in graph.nodes}

    # Lista de vértices no visitados
    unvisited = list(graph.nodes)

    while unvisited:
        # Seleccionar el vértice no visitado con distancia mínima
        current = min(unvisited, key=lambda node: distancia[node])
        unvisited.remove(current)

        # Actualizar las distancias de los vértices vecinos
        for vecino, peso in graph.edges[current]:
            new_distancia = distancia[current] + peso

            if new_distancia < distancia[vecino]:
                distancia[vecino] = new_distancia
                padre[vecino] = current

    return distancia, padre

def get_path(padre, destination):
    path = [destination]
    while padre[destination] is not None:
        destination = padre[destination]
        path.insert(0, destination)
    return path

def measure_time():
    # Código para medir el tiempo de ejecución
    start_time = time.time()

    grafo = Graph()
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_vertex("D")
    grafo.add_vertex("E")
    grafo.add_vertex("F")
    grafo.add_vertex("G")
    grafo.add_edge("A", "B", 4)
    grafo.add_edge("A", "C", 7)
    grafo.add_edge("B", "C", 1)
    grafo.add_edge('A', 'B', 2)
    grafo.add_edge('A', 'C', 8)
    grafo.add_edge('A', 'F', 4)
    grafo.add_edge('B', 'C', 1)
    grafo.add_edge('B', 'D', 15)
    grafo.add_edge('C', 'D', 11)
    grafo.add_edge('C', 'F', 23)
    grafo.add_edge('D', 'E', 5)
    grafo.add_edge('E', 'F', 2)
    grafo.add_edge("A", "G", 6)
    grafo.add_edge("C", "E", 3)

    start_node = 'A'
    results, padre = dijkstra(grafo, start_node)

    for node, distancia in results.items():
        if node != start_node:
            path = get_path(padre, node)
            print(f"El camino más corto de {start_node} a {node}: {path}, con distancia de: {distancia}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo de ejecución: {elapsed_time} segundos")

measure_time()