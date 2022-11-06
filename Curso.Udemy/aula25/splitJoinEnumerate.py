"""
Split, Join, Enumerate em Python
*Split - Dividir uma string #str
*Join - juntar uma lista #str
*Enumerate - Enumerar elementos da lista #list / iteraveis
"""

"""
Funcao Split
"""
'''
string = 'O Brasil é o pais do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
print(lista_1)
print(type(lista_1))
lista_2 = string.split(',')
print(lista_2)
cont = 0
for valor in lista_1:
    print(lista_1.count(valor), '=', valor)

"""
palavra = ' '
contagem = 0

for valor in lista_1:
    quantidadeVezes = lista_1.count(valor)

    if contagem < quantidadeVezes:
        contagem = quantidadeVezes
        palavra = valor
print(f'A palavra que mais apareveu é: {palavra} apareceu {contagem} vezes')
"""

for valor in lista_2:
    print(valor.strip().capitalize(), type(valor), type(lista_2))
'''

'''
Funcao Join
'''
"""
string = 'O Brasil é penta'
lista = string.split(' ')
print(lista)
string2 = ','.join(lista)
print(string2)
"""

"""
funcao enumerate
"""
'''
string = 'O Brasil é penta'
lista = string.split(' ')

for pos, valor in enumerate(lista):
    print(f'O {valor} esta na posição {pos}')
'''
'''
lista = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for indice, valor in enumerate(lista):
    print(indice, valor)
'''
lista = [
    [0, 'Denis','marcos'],
    [1, 'joyce', 'lucas'],
    [2, 'Marta', 'joao']
]
for indice, valor, nome in lista:
    print(indice, valor, nome)

'''
Desempacotamento
'''
lista2 = ['Denis', 'Diogo', 'dos', 'Santos']
v1, v2, v3, v4 = lista2
print(v4, v3, v2, v1)
