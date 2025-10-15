import networkx as nx
import matplotlib.pyplot as plt

# 1. Crea un grafo no dirigido (Graph)
G = nx.Graph()

# 2. Añade los nodos y las aristas
nodos = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(nodos)

aristas = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'E'),
    ('E', 'A')
]
G.add_edges_from(aristas)

# 3. Calcula e imprime las propiedades
print("--- Propiedades del Grafo G ---")
# Número total de nodos
num_nodos = G.number_of_nodes()
print(f"1. Número total de nodos: {num_nodos}")

# Número total de aristas
num_aristas = G.number_of_edges()
print(f"2. Número total de aristas: {num_aristas}")

# Grado del nodo 'A' (nx.degree(G, 'nodo'))
grado_A = G.degree('A')
print(f"3. Grado del nodo 'A': {grado_A}")

# Vecinos del nodo 'E' (list(G.neighbors('nodo')))
vecinos_E = list(G.neighbors('E'))
print(f"4. Vecinos del nodo 'E': {vecinos_E}")

# 4. Visualiza el grafo
plt.figure(figsize=(5, 4))
# 'with_labels=True' asegura que los nombres de los nodos se muestren
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_weight='bold')
plt.title("Grafo Básico No Dirigido")
plt.show()