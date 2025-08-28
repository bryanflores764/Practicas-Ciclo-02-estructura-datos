# Ejercicio 7: 
# Crear una lista de calificaciones de un estudiante y calcular estadísticas: 
# Instrucciones: 
# • Crear una lista con 8 calificaciones (números del 0 al 10) 
# • Calcular y mostrar: promedio, calificación máxima, calificación mínima 
# • Contar cuántas calificaciones están por encima del promedio 
# • Ordenar las calificaciones de mayor a menor 

calificaciones = [8,8,9,8,6,]
promedio = sum(calificaciones) / len(calificaciones)

# Calificación máxima y mínima
maxima = max(calificaciones)
minima = min(calificaciones)

# Contar cuántas calificaciones están por encima del promedio
mayores_promedio = sum(1 for nota in calificaciones if nota > promedio)

# Ordenar las calificaciones de mayor a menor
ordenadas = sorted(calificaciones, reverse=True)

# Mostrar resultados
print("Estadísticas del estudiante 👨‍🎓")
print("-" * 25)
print(f"Promedio: {promedio:.2f}")
print(f"Calificación máxima: {maxima}")
print(f"Calificación mínima: {minima}")
print(f"Cantidad de calificaciones por encima del promedio: {mayores_promedio}")
print(f"Calificaciones ordenadas de mayor a menor: {ordenadas}")