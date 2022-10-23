'''
For in em python
interando string com for
Funcao range (start=0, stop, step=1)

'''
texto = 'Python'
'''
c=0
while c < len(texto):
    print(texto[c])
    c += 1
 para este tipo de incremento nao utilizar while

for pos, c in enumerate(texto):

    print(f'A letra {c} esta na posição {pos}')
 
for numero in range(20, 10,-1):
    print(numero)
'''
nova_string = ''
for dados in texto:
    if dados == 't' or dados == 'h':
        continue
        nova_string += dados.upper()
    else:
        nova_string += dados
print(nova_string)
