'''
While / Else - aula 8
contadores
acumuladores
'''
contador = 1
acumulador = 1
while contador <= 10:
    if contador == 5:
        break
    print(f'contador {contador}')
    print(f'acumulador{acumulador}')
    acumulador += contador
    contador += 1
#print(acumulador)
else:
    print('cheguei no else')
    contador = 0
print('nao executou else.')

