'''
interpolação basica de string
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
'''
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O valor %d em hexadecimal é %04X' % (1500, 1500))