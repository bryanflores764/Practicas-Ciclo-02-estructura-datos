import networkx as nx
import matplotlib.pyplot as plt

# 1. Crea un grafo no dirigido simple (se puede usar Graph)
P = nx.Graph()

# 2. Añade las aristas ponderadas
# Formato: (Nodo1, Nodo2, {'weight': Peso})
rutas_ponderadas = [
    ('O', 'A', {'weight': 5}),
    ('O', 'B', {'weight': 1}),
    ('A', 'C', {'weight': 2}),
    ('B', 'A', {'weight': 2}),
    ('B', 'D', {'weight': 3}),
    ('C', 'D', {'weight': 1}),
    ('D', 'E', {'weight': 4})
]
P.add_edges_from(rutas_ponderadas)

# 3. Aplica el algoritmo de Dijkstra
origen = 'O'
destino = 'E'

# Camino más corto (nodos del camino)
# 'weight' indica que use los valores de los pesos en la arista
camino_dijkstra = nx.shortest_path(P, source=origen, target=destino, weight='weight')

# Distancia total (longitud del camino)
distancia_dijkstra = nx.shortest_path_length(P, source=origen, target=destino, weight='weight')

# 4. Imprime el resultado
print("--- Análisis de Camino Más Corto (Dijkstra) ---")
print(f"Origen: {origen}, Destino: {destino}")
print(f"1. El camino más corto es: {camino_dijkstra}")
print(f"2. La distancia total mínima es: {distancia_dijkstra}")


# Visualización (incluyendo los pesos)
pos = nx.spring_layout(P, seed=42) # Para posiciones reproducibles
plt.figure(figsize=(7, 5))
nx.draw(P, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_weight='bold')

# Añade etiquetas de peso a las aristas
edge_labels = nx.get_edge_attributes(P, 'weight')
nx.draw_networkx_edge_labels(P, pos, edge_labels=edge_labels)

plt.title("Grafo Ponderado y Camino Mínimo (Dijkstra)")
plt.show()