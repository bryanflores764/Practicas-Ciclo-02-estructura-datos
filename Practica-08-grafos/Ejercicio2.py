import networkx as nx
import matplotlib.pyplot as plt

# 1. Crea un grafo dirigido (DiGraph)
D = nx.DiGraph()

# 2. Añade las aristas dirigidas
rutas = [
    ('Madrid', 'Barcelona'),
    ('Madrid', 'Sevilla'),
    ('Barcelona', 'Valencia'),
    ('Sevilla', 'Málaga'),
    ('Valencia', 'Madrid'),
    ('Málaga', 'Barcelona'),
    ('Málaga', 'Granada')
]
D.add_edges_from(rutas)

# 3. Encuentra el camino más corto (Madrid a Granada)
origen = 'Madrid'
destino = 'Granada'

print("--- Rutas en el Grafo Dirigido D ---")
try:
    # nx.shortest_path encuentra el camino con el menor número de aristas (no ponderado)
    camino = nx.shortest_path(D, source=origen, target=destino)
    print(f"1. Camino más corto de {origen} a {destino}: {camino}")
except nx.NetworkXNoPath:
    print(f"1. ¡Advertencia! No existe un camino de {origen} a {destino}.")


# 4. Verifica si existe un camino (Granada a Sevilla)
origen_verif = 'Granada'
destino_verif = 'Sevilla'

# nx.has_path() devuelve True o False
existe_camino = nx.has_path(D, source=origen_verif, target=destino_verif)
print(f"2. ¿Existe un camino de {origen_verif} a {destino_verif}? {existe_camino}")

# Visualización (Opcional, pero útil para entender)
pos = nx.spring_layout(D) # Define la posición de los nodos
plt.figure(figsize=(7, 5))
# Dibujamos con 'connectionstyle' curvo para evitar superposición en aristas opuestas
nx.draw(
    D, pos, with_labels=True, node_color='lightcoral', node_size=2000,
    arrowsize=20, font_weight='bold', edge_color='gray',
    connectionstyle='arc3, rad = 0.1' 
)
plt.title("Grafo Dirigido de Rutas")
plt.show()