'''nome = input('Qual o seu nome: ').upper()
#mensagem = 'O seu nome e {}'.format(nome)
print(f'O seu nome e {nome=}') #retorna o nome da variavel e o valor que contem ela
print(type(nome))'''

try:
    nume_1 = int(input('Digite um numero: '))
    nume_2 = int(input('Digite outro numero: '))
except:
    print('ERRO')
else:
    soma = nume_1 + nume_2
    print(nume_1 + nume_2)
