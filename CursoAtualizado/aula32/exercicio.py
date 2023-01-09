"""
Faça um programa que peca ao usuario para digitar um numero inteiro, 
informe se este numero e par ou impar. Caso o usuario não digite um numero
inteiro, informe que não é um numero inteiro.
"""

try:
    numero = int(input('Digite um numero'))
except:
    print('não é um numero inteiro')
else:
    par = numero % 2 == 0
    if par:
        print('numero par')
    else:
        print('Numero impar')
print('~='*10)

entrada = input('Digite um numero inteiro')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    texto = 'Impar'
    if par_impar:
        texto = 'Par'
    print(f'O numero {entrada_int} e um numero {texto}')
else:
    print('Não é um numero inteiro')

"""
Faca um programa que pergunte a hora ao usuario e, baseando - se no horário
descrito, exiba a saudação apopriada. EX.
Bom dia 0-11; Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    horario = int(input('Digite um horario'))
except:
    print('Digite um horario valido')
else:
    if 0 <= horario <= 11:
        print('Bom dia')
    elif 12 <= horario <= 17:
        print('Boa Tarde')
    elif 18 <= horario <= 23:
        print('Boa noite')
    else:
        print('Horario invalido')
print('~='*10)

horario = input('Digite um horario')

if horario.isdigit():
    horario_int = int(horario)
    if 0 <= horario_int <= 11:
        print('Bom dia')
    elif 12 <= horario_int <= 17:
        print('Boa Tarde')
    elif 18 <= horario_int <= 23:
        print('Boa noite')
    else:
        print('Horario invalido')

else:
    print('Digite um horario valido')
"""
Faca um programa que pergunte o primeiro nome do usuario. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal" 
maior que 6 letras escreva " seu nome é grande".
"""
try:
    nome = str(input('Digite seu nome'))
except:
    print('Digite um nome valido')
else:
    letras = len(nome)
    if letras <= 4:
        print('Seu nome é curto')
    elif letras <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')

