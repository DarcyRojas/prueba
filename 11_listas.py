#ARREGLOS CLASE 21MARZO
primera_lista = ['Manzana', 'Banano']
print(primera_lista)
nombres = ["Cesar", "Octavio", "Luisa"]
print(nombres)

#listas numericas entereas o flotantes
lista1 = [2, 4, 89, 1000, 3.14]
print(lista1)
lista2 = ['a', 123, 'A', 3.1416, 'Palabra', True, 1000]
print(lista2)

# Tamaño de una lista con la función (len):
print("Tamaño de lista:")
print(len(lista1))
print(len(lista2))

# Tipo de dato lista:
print('Tipo de dato lista:')
print(type(lista1))
print(type(lista2))

# Otra lista de un arreglo a un formato lista 
print("Función list():")
num = [1, 2, 3, 4, 5]
print(num)
num2 = list({1, 2, 3, 4, 5})

print(num2)
print("Index list:")
print(num[0])
print(num[0:3])
print(num[-1::-1]) # :: para que vaya corriendo de 1 en 1 

print("Uso de función IN:")
print(3 in num)
print(10 in num)
num1 = num
print(num)
print(num1)
print(num2)
print(num1 is num)
print(num2 is num)
