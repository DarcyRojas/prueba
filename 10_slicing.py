# CLASE 21MARZO
nombre = 'Cesar Quintero'
# INDEXING:
# Posición índice de 'C' es cero:
print(nombre[0])
print(nombre[4])

# SLICING:
print(nombre[1:4]) #cuando necesito la posición final le pongo un numero más. 
print(nombre[2:7])
print(nombre[7:12])
print(nombre[0:14])
print(nombre[0:]) #me imprime toda la variable si lo dejo con : al final

print(nombre[0:7:2]) #CsrQ
print(nombre[0:13])
print(nombre[0:13:2])
print(nombre[0:13:3])

# Regresivo:
print('Regresivo:')
print(nombre[-1:-9:-1])