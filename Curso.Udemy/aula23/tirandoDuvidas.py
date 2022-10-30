"""
secreto += 'a'
secreto += 'b'
secreto += '*'
"""

secreto = 'python'
palavraSecreta = ''
letrasDigitadas = ['p','y','o','t','h','a','e','n','u']
for palavra in secreto:
    if palavra in letrasDigitadas:
        palavraSecreta += palavra
    else:
        palavraSecreta += '*'


print(secreto)
print(palavraSecreta)
if secreto == palavraSecreta:
    print('Voce ganhou')


