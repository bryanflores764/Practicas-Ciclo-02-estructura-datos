# Ejercicio 9: 
# Crear un programa que trabaje con una cadena de texto usando slicing: 
# Instrucciones: 
# • Usar la frase: "Universidad de Oriente - El Salvador" 
# • Extraer solo "Universidad" 
# • Extraer solo "El Salvador" 
# • Mostrar la frase completa al revés 
# • Mostrar cada tercera letra de la frase

# Frase de ejemplo
frase = "Universidad de Oriente - El Salvador"

# Extraer solo "Universidad"
print("Parte 1:", frase[:11])

# Extraer solo "El Salvador"
print("Parte 2:", frase[-11:])

# Mostrar la frase completa al revés
print("Frase al revés:", frase[::-1])

# Mostrar cada tercera letra de la frase
print("Cada tercera letra:", frase[2::3])