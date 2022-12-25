
*Seu nome tem {n} letras
*A primeira letra do seu nome é {letra}
*A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
*Exiba "Desculpe, você deixou campos vazios.
"""

nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

print(f'Seu nome é {nome}')
print(f'Seu nome invertido é {nome[::-1]}')
if(' ' in nome):
    print(f'Seu nome contem espaco vazio')
else:
    print(f'Seu nome nao contem espaço vazio')
print(f'Seu nome contem {len(nome)} letras')
print(f'A primeira letra do seu nome e {nome[0]}')
print(f'A ultima letra do seu nome é {nome[-1]}')
if(nome == ' ' or idade == ' '):