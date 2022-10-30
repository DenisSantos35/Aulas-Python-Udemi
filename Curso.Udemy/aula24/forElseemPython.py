"""
For / Else  em Python
"""

"""
for pos,texto in enumerate(variavel):
    print(pos, texto)
    if pos == 1:
        continue
    print(pos,texto)
"""
variavel = ['Denis Santos', 'Joyce', 'Maria']
"""
comecaComJ = False
for valor in variavel:
    if valor.lower().startswith('j'):
        comecaComJ = True
        novoNome = valor.replace('J', 'D')
        print(f'Nome {valor} comeca com J', novoNome)
    else:
        print(f'O nome {valor} não comeca com J')
if comecaComJ:
    print('Exite uma palavra que comeca com J.')
else:
    print('Não existe uma palavra que comeca com J.')
"""
for valor in variavel:
    if valor.lower().startswith('j'):
        print('Existe palavra que comeca com J')
        break
else:
    print('Não existe palavra que comeca com J')
