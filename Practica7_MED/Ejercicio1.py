class NodoCategoria:
    def __init__(self, id_categoria, nombre):
        self.id = id_categoria
        self.nombre = nombre
        self.izquierdo = None
        self.derecho = None

# Insertar una categoría
def insertar(raiz, id_categoria, nombre):
    if raiz is None:
        return NodoCategoria(id_categoria, nombre)
    if id_categoria < raiz.id:
        raiz.izquierdo = insertar(raiz.izquierdo, id_categoria, nombre)
    elif id_categoria > raiz.id:
        raiz.derecho = insertar(raiz.derecho, id_categoria, nombre)
    return raiz

# Buscar una categoría
def buscar(raiz, id_categoria):
    if raiz is None or raiz.id == id_categoria:
        return raiz
    if id_categoria < raiz.id:
        return buscar(raiz.izquierdo, id_categoria)
    return buscar(raiz.derecho, id_categoria)

# Recorrido Inorder (muestra categorías en orden alfabético si los ID están organizados)
def inorder(raiz):
    if raiz:
        inorder(raiz.izquierdo)
        print(f"ID:{raiz.id}, Categoría: {raiz.nombre}")
        inorder(raiz.derecho)

# Ejemplo de uso
raiz = None
categorias = [
    (50, "Biblioteca"),
    (30, "Literatura"),
    (20, "Novela"),
    (40, "Poesía"),
    (70, "Ciencia"),
    (60, "Matemáticas"),
    (80, "Historia")
]

for id_categoria, nombre in categorias:
    raiz = insertar(raiz, id_categoria, nombre)

print("Listado de categorías (Inorder):")
inorder(raiz)

print("\nBuscar categoría con ID 60:")
resultado = buscar(raiz, 60)
if resultado:
    print(f"Encontrada: {resultado.nombre}")
else:
    print("Categoría no encontrada")