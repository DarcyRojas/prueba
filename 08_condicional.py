# Condicional if clase 20marzo
#if('prueba logica') ejm podría ser numer=3
numero = int(input('Sr usuario, digite un numero: '))
if(numero>50): #solo para IF se pone la conidición y se ponen : despues de cerrar el paretesis.
  print('Verdadero') #aparece un margen de sangría y se completa en este caso con el print
else:
  print('falso') #Si quiero que me de falso sería con else (s como el si no es verdaero entonces es falso)

print('La instruccion "IF" terminó. ')

#if anidado
adivinar = 42
numero = int(input('Sr usuario, digite un numero: '))
if(numero > adivinar):
  print('Bajele el color')
elif (numero < adivinar): #aqui se anida el else con if y queda elif
  print('subale el volumen')
else:
  print('verdadero') # wsy si no se cumplen ninguna condición se finaliza con else

  
  #if anidado 2
if (numero >= adivinar):
  if (numero > adivinar):
    print('Coloque un número menor.')
  else: #SI NO ES LO ANTERIOR
    print('Acertado!!!')
else:
  print('Coloque un número mayor')
# Fin del IF.

print('La instrución "IF" terminó. ')
