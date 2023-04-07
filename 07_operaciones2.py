#CLASE 17marzo
number = int(input('Digite un número: '))

#OPERACIONES RELACIONALES O DE COMPARACION
print(number > 3)  #pregunta si number es mayor a 3
print(number >= 3)  #pregunta si number es mayor o igual a 3
print(number < 3)  #pregunta si number es menor a 3
print(number <= 3)  #pregunta si number es menor o igual a 3
print(number == 3)  #pregunta si number es igual o igual a 3
print(number != 3)  #pregunta si number no es igual o diferente a 3-

#OPERACIONES LOGICAS
# Conjunción (and &), Disyunción (or, |), # Negación (not), # Or exclusiva (^),

print("Operaciones lógicas.")

# Conjunción (and &) and da veradero cuando todo es verdadero
print('Conjuncion:')
print(False and True)
print((number >= 3) and False)
#puedo cambiar el and por el & como ejem abajo
print(True & True)
print(False and False)
print(False & False)
print(number > 3 and number < 10)

# Disyunción (or, |) #clase 20marzo
print('Disyunción:')
print(False or False)  #si una de las entradas es true el resultado es true
print(False or True)
print(number <= 3 or number >= 10)  # cuando pongo intervalos
print(not (number <= 3 | number >= 10))

# Negación (not)
print('Negación:')
print(not (True))

# Or exclusiva (^)
print('Or exclusiva:')
print(False ^ False)
print(False ^ True)
print(True ^ False)
print(True ^ True)

#OPERACIONES DE PERTENENCIA
# in - pregunta si un valor se encuentra detro de una variable
print('Operador in:')
nombre = 'Cesar Quintero'
print('Q' in nombre)  #pregunta si Q esta en la variable nombre
print('z' in nombre)  #pregunta si z esta en la variable nombre
