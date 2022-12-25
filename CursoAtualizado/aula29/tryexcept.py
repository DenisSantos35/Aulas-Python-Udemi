"""
Introdução ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao executar
"""
numero_str = input('Vou dobrar o numero que você digitar: ')
try:    
    numero_float = float(numero_str)
    print(f'O dobro do numero {numero_str} é {numero_float * 2:.0f}')
except:
    print('isso não é um numero')   