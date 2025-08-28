# ÍNDICES y SLICING 
# Ejercicio 8: 
# Dada la siguiente lista de días de la semana, realizar operaciones de slicing: 
# dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", 
# "Sábado", "Domingo"] 
# Instrucciones:  
# a) Mostrar los primeros 3 días  
# b) Mostrar los últimos 2 días  
# c) Mostrar los días laborales (Lunes a Viernes)  
# d) Mostrar el fin de semana  
# e) Mostrar todos los días en orden inverso  
# f) Mostrar un día sí y otro no (días pares) 


# a) Muestra la lista de días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# a) Muestra los primeros 3 días
print("Primeros 3 días:", dias[:3])

# b) Muestra los últimos 2 días
print("Últimos 2 días:", dias[-2:])

# c) Muestra los días laborales (Lunes a Viernes)
print("Días laborales:", dias[:5])

# d) Muestra el fin de semana
print("Fin de semana:", dias[-2:])

# e) Muestra todos los días en orden inverso
print("Días en orden inverso:", dias[::-1])

# f) Muestra un día si y otro no (días pares)
print("Un día sí y otro no:", dias[::2])