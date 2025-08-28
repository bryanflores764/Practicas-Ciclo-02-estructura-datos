#  PRINT 
# Ejercicio 1: 
# Imprimir la siguiente estrofa de la canción "Bendita tierra" de Kime, respetando el siguiente 

# formato: 
# Vivo enamorado de este suelo, 
# No me canso de tu luna y de tu cielo, 
# Porque yo elegí aquí sembrar mis sueños 
# Porque Dios llenó de magia este pueblo 
# Voy desde cipote entre "la yerba" 
# En mi sangre llevo todos tus paisajes 

# Instrucciones: 
# • Usar la función print() 
# • Respetar exactamente el formato mostrado (cursivas, comillas) 
# • Agregar comentarios explicando cada línea de código

#codigo ANSI 

I = "\033[3m"
R = "\033[0m"

#Primera linea en cursiva

print(f"{I}Vivo enamorado de este suelo{R}")

#segunda linea en cursiva

print(f"{I}No me canso de tu luna y de tu cielo,{R}")

#tercera linea en cursiva

print(f"{I}Porque yo elegí aquí sembrar mis sueños{R}")

#cuarta linea en cursiva

print(f"{I}Porque Dios llenó de magia este pueblo{R}")


#quinta linea en cursiva (respetando las comillas internas de la palabra yerba)
print(f"{I}Voy desde cipote entre \"la yerba\" {R}")

#sexta linea en cursiva

print(f"{I}En mi sangre llevo todos tus paisajes {R}")