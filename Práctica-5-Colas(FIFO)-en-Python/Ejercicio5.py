class cola:
    def __init__(self):
        self.elementos = []
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def encolar(self, item):
        self.elementos.append(item)
    
    def desencolar(self):
        return self.elementos.pop(0) if not self.esta_vacia() else "Cola vacía"

cola_red = cola()
cola_red.encolar("Orden de tacos")
cola_red.encolar("Orden de pizza")
cola_red.encolar("Orden de amburguesa")

print("Se cocina:", cola_red.desencolar())
print("En espera:", cola_red.elementos)