#operadores in e not in
#strings sao interaveis
# 0 1 2 3 4 5
# o t a v i o 
#-6-5-4-3-2-1
'''
frase = 'Denis Diogo dos Santos'
print(frase[::-1])
lista = frase.split(' ')
print(lista[-3])
print(lista)
nome = lista.pop(0)
print(nome)
sobrenome = " ".join(lista)
print(sobrenome)
print(' ' in frase)
'''
nome = input('Digite um nome: ')
encontrar = input('O que deseja encontrar? ')
if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print('{} nao esta em {}'.format(encontrar, nome))