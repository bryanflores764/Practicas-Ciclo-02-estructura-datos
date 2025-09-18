import random

random.seed(42)

# Generando clientes con tuplas 
clientes = [
    ("Cliente 1", random.randint(1,10)),
    ("Cliente 2", random.randint(1,10)),
    ("Cliente 3", random.randint(1,10)),
    ("Cliente 4", random.randint(1,10)),
    ("Cliente 5", random.randint(1,10))
]

tiempo_acumulado = 0  # Tiempo que el cajero ha trabajado
tiempo_espera = []    # Lista para guardar tiempos de espera de cada cliente
tiempo_servicio = []  # Guarda los tiempos de servicio del cajero

for nombre, servicio in clientes:
    # Tiempo de espera del cliente actual en lo que el cajero ha trabajado
    espera = tiempo_acumulado
    tiempo_espera.append(espera)
    tiempo_servicio.append(servicio)

    print(f"{nombre}: tiempo de servicio {servicio}min, tiempo de espera = {espera} min")

    # actualizacion acumulada: despues de atender al cliente en el cajero
    tiempo_acumulado += servicio

# calculos finales
promedio_espera = sum(tiempo_espera) / len(tiempo_espera)
promedio_servicio = sum(tiempo_servicio) / len(tiempo_servicio)

print(f"\nPromedio de espera: {promedio_espera:.2f} min")
print(f"Promedio de servicio: {promedio_servicio:.2f} min")