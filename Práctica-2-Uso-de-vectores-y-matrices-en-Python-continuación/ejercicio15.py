# CONJUNTOS (SETS) 
# Ejercicio 15: 
# Trabajar con conjuntos de materias de diferentes carreras: 
# Instrucciones: 
# • Crear 3 conjuntos: materias de Software, Sistemas y Datos 
# • Cada conjunto debe tener al menos 6 materias 
# • Encontrar materias comunes entre todas las carreras 
# • Encontrar materias exclusivas de cada carrera 
# • Crear la unión de todas las materias 
# • Mostrar cuántas materias únicas hay en total 

# Ejercicio 15: Materias de diferentes carreras

# Crear 3 conjuntos de materias
software = {"Programación", "Base de Datos", "Redes", "Ingeniería de Software", "Matemáticas Discretas", "Sistemas Operativos"}
sistemas = {"Programación", "Estructura de Datos", "Redes", "Arquitectura de Computadoras", "Sistemas Operativos", "Matemáticas"}
datos = {"Programación", "Estadística", "Base de Datos", "Minería de Datos", "Inteligencia Artificial", "Matemáticas"}

# Materias comunes entre todas las carreras
comunes = software & sistemas & datos
print("Materias comunes en todas las carreras:", comunes)

# Materias exclusivas de cada carrera
print("Exclusivas de Software:", software - (sistemas | datos))
print("Exclusivas de Sistemas:", sistemas - (software | datos))
print("Exclusivas de Datos:", datos - (software | sistemas))

# Unión de todas las materias
union_materias = software | sistemas | datos
print("\nUnión de todas las materias:", union_materias)

# Número total de materias únicas
print("Total de materias únicas:", len(union_materias))