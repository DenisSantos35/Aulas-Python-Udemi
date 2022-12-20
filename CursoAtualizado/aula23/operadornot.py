'''
Operador lógico "not"
Usado para inverter expressções
not True = False;
not False = True;
'''

senha = input('Senha: ')

if senha != '123456':
    print('Senha incorreta')

if not senha:
    print('Voce nao digitou nada')
print(not True)
print(not False)
print(not 0)
print(not None)