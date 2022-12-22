'''
Formatacao basica de strings
s - string
d - int
f - float
.<numeros de digitos>f
x ou X - hexadecimal
(caracter)(<>^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
sinal - + ou - 
ex.: 0>-100,.1f
conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: ^10}')
print(f'{1000.56849712564:+.2f}')
print(f'O hexadecimal de 1500 e {1500:04X}')