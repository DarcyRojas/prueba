#CLASE 17marzo
#OPERACIONES ARITMETICAS
# SUMA +, RESTA -, MULTI *, DIVI /, DIV ENTERA //, Jerarquia: (), **, * /, + - ejm
# RESIDUO O MÓDULO %, POTENCIA **.
number = int(input('Digite un número: '))
'''print(f'La suma con 2 es: {number + 2}')
print(f'La resta con 2 es: {number - 2}')
print(f'La multiplicación con 2 es: {number * 2}')
print(f'La división con 2 es: {number / 2}')
print(f'La división ENTERA con 2 es: {number // 2}')
print(f'El residuo con 2 es: {number % 2}')
print(f'La potencia con 2 es: {number ** 2}')'''

#OPERACIONES DE ASIGNACION
contador = 1
'''print(f'antes de += {contador}')'''
contador += 1  # contador = contador + 1 (+= oper. asignación incremental)
'''print(f'despues de += {contador}')'''
contador = 9
contador -= 1  # contador = contador - 1 (-= oper. asignación decremental)

number += 1
print(f'Operador incremental += el resultado es: {number}')
number -= 1
print(f'Al usar el operador decremental -= el resultado es: {number}')
number *= 2
print(f'Al usar el operador *= el resultado es: {number}')
number /= 2
print(f'Al usar el operador /= el resultado es: {number}')
number //= 2
print(f'Al usar el operador //= el resultado es: {number}')
number %= 3
print(f'Al usar el operador %= el resultado es: {number}')
number **= 2
print(f'Al usar el operador **= el resultado es: {number}')
