"""
* Enumerate - Enumerar elementos da lista #list
"""
#indices   0      1       2
lista = [
    ['Edu', 'Joao', 'Luiz'], #0
    ['Maria', 'Aline', 'Joana'],#1
    ['willian', 'marcos', 'joy'] #2
]
enumerada = list(enumerate(lista))
print(enumerada[0][1][2])

'''
[ <--Enumerate
    0   1
    (0, ['Edu', 'Joao', 'Luiz']), 0
           0       1      2
    (1, ['Maria', 'Aline', 'Joana']),1
    (2, ['willian', 'marcos', 'joy'])2
]
'''
#   start  , val lista         lista, start
for indice, valor in enumerate(lista, 50):
    for pos, val in enumerate(valor, 100):
        print(f'Lista = [{indice}][{pos}], {val}')
"""
Lista = [50][100], Edu
Lista = [50][101], Joao
Lista = [50][102], Luiz
Lista = [51][100], Maria
Lista = [51][101], Aline
Lista = [51][102], Joana
Lista = [52][100], willian
Lista = [52][101], marcos
Lista = [52][102], joy
"""
#   start  , val lista         lista, start
for valor in enumerate(lista, 50):
    print(f'{valor}')
"""
(50, ['Edu', 'Joao', 'Luiz'])
(51, ['Maria', 'Aline', 'Joana'])
(52, ['willian', 'marcos', 'joy'])
"""

#   start  , val lista         lista, start
for valor in enumerate(lista, 50):
    valorEnumrado, minhaLista = valor
    print(valorEnumrado, minhaLista)
"""
50 ['Edu', 'Joao', 'Luiz']
51 ['Maria', 'Aline', 'Joana']
52 ['willian', 'marcos', 'joy']
"""
#   start  , val lista         lista, start
for valor in enumerate(lista, 50):
    valorEnumrado, minhaLista = valor
    print( minhaLista)
"""
['Edu', 'Joao', 'Luiz']
['Maria', 'Aline', 'Joana']
['willian', 'marcos', 'joy']
"""
#   start  , val lista         lista, start
for valor in enumerate(lista, 50):
    valorEnumrado, minhaLista = valor
    nome1, nome2, nome3 = minhaLista
    print(nome1, nome2, nome3)
"""
Edu Joao Luiz
Maria Aline Joana
willian marcos joy
"""
