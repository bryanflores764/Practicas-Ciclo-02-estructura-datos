# VARIABLES 
# Ejercicio 4: 
# Crear un programa que declare variables de diferentes tipos de datos básicos y muestre su 
# información: 
# Instrucciones: 
# • Crear al menos una variable de cada tipo: int, float, str, bool 
# • Usar la función type() para mostrar el tipo de cada variable 
# • Mostrar el valor y tipo de cada variable en formato legible 
# • Realizar operaciones básicas entre variables compatibles 
# Ejemplo de salida esperada: 
# Variable: edad = 20, Tipo: <class 'int'> 
# Variable: promedio = 8.5, Tipo: <class 'float'> 
# Variable: nombre = "Juan", Tipo: <class 'str'> 
# Variable: activo = True, Tipo: <class 'bool'> 

#Declaracion de variables
edad = 15                  #int
promedio = 6.7             #float
nombre = "bryan"           #string
activo = True              #bool

#Mostrando el valor y cada tipo de dato para cada variable

print(f"Variable: edad = {edad}, Tipo: {type(edad)}")
print(f"Variable: promedio = {promedio}, Tipo: {type(promedio)}")
print(f"Variable: nombre = {nombre}, Tipo: {type(nombre)}")
print(f"Variable: activo = {activo}, Tipo: {type(activo)}")

#Operaciones basicas con las variables

print("\n---Operaciones Basicas ---")
print(f"Suma edad + promedio = {edad+promedio}") #int + float
print(f"Multiplicacion de edad * 2={edad*2}")       #int *int
print(f"Concatenacion de nombre + 'Pérez' = {nombre + "Pérez"}") #string + string
print(f"Negacion de activo = {not activo}")#operacion logica con bool