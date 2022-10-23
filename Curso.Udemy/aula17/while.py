'''while True:
    nome = str(input('Qual o seu nome:  '))
    print(f'Olá {nome}')'''

'''x = 0
while x <= 10:
    if x == 3:
        x += 1
        continue
    print(x)
    x += 1

print('>>FIM<<')'''

# tabela com while

'''x = 0
y = 0
cont = 0

while x < 10:
    while y <= 4:
        cont += 1
        print (f'{cont}',end='')
        y += 1
    print()
    x += 1
    y=0
    cont=0'''

#calculadora com while
from time import sleep

while True:
    print()
    num1 = str(input('Digite um numero: '))
    num2 = str(input('Digite outro numero: '))
    if num1.isnumeric() and num2.isnumeric():
        num1 = float(num1)
        num2 = float(num2)
    else:
        continue
    operador = str(input('Qual operação deseja fazer? [+];[-];[*];[/]')).strip()
    while operador not in '+-*/':
        operador = str(input('Qual operação deseja fazer? [+];[-];[*];[/]')).strip()
    if operador == '+':
        print(num1+num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        if num1 == 0 or num2 == 0:
            print('Não é possivel realizar operação!!!')
        else:
            print(num1 / num2)
    continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()
    sleep(2)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if continuar == 'S':
        continue
    else:
        print('Finalizando calculadora')
        break
print('Obrigado por utilizar a calculadora')





