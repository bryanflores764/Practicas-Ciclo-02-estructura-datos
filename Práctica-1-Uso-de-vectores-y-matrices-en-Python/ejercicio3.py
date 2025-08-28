# INPUT 
# Ejercicio 3: 
# Sin crear variables adicionales, solicitar que el estudiante de la Universidad de Oriente ingrese la 
# siguiente información: (Nombres), (Apellidos), (Materia) y (Carnet) y que se imprima de la 
# siguiente manera: 
# Hola, Bienvenido [Nombres] [Apellidos] gracias por registrarte a 
# la materia de: [Materia], tu usuario para ingresar es: 
# [Carnet]@univo.edu.sv 
# Instrucciones: 
# • No crear variables intermedias 
# • Usar directamente input() dentro del print() 
# • Usar f-strings para el formateo

print(
    f"Hola bienvenido {input('Ingrese sus Nombres: ')} {input('Ingresa tus Apellidos: ')} "
    f"gracias por registrarte ala materia de:{input('Ingresa la Materia: '),}"
    f"tu usario para ingresar es: {input('Ingresa tu numero de Carnet: ')}@univo.edu.sv"
)