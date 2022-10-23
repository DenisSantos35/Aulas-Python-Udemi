nome = 'Denis'
idade = 32
anoAtual = 2022
anoNascimento = anoAtual - idade
peso = 50
altura = 1.68
imc = peso/(pow(altura,2))

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} Kg.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {anoNascimento}')
