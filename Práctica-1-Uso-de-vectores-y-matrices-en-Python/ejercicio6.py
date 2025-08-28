# LISTAS 
# Ejercicio 6: 
# Crear una lista con los nombres de 5 materias de Ingeniería de Software y realizar las siguientes 
# operaciones: 
# Instrucciones:  
# a) Mostrar la lista completa  
# b) Agregar 2 materias más usando append()  
# c) Insertar una materia en la posición 2 
# d) Eliminar la última materia usando remove()  
# e) Mostrar el número total de materias  
# Materias sugeridas: Programación, Estructura de Datos, Base de Datos, Ingeniería de Software, 
# Redes


# Ejercicio 6: Trabajar con listas de materias de Ingeniería de Software

# a) Crear lista con 5 materias
materias = ["Programación", "Estructura de Datos", "Base de Datos", "Ingeniería de Software", "Redes"]

# b) Agregar 2 materias más usando append()
materias.append("Sistemas Operativos")
materias.append("Inteligencia Artificial")
print("Lista después de agregar 2 materias:", materias)

# c) Insertar una materia en la posición 2
materias.insert(2, "Matemáticas Discretas")
print("Lista después de insertar una materia en la posición 2:", materias)

# d) Eliminar la última materia usando remove()
# Primero identificamos el nombre de la última materia
ultima_materia = materias[-1]
materias.remove(ultima_materia)
print("Lista después de eliminar la última materia:", materias)

# e) Mostrar el número total de materias
print("Número total de materias:",len(materias))