#        indices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma' #valor iteravel
tamanho_frase = len(frase)
print(tamanho_frase)
contador = 0
nova_string = ''
'''while contador < tamanho_frase:
    #print(frase[contador], contador,end="")
    nova_string += frase[contador]
    print(nova_string)
    contador += 1'''
usuario = str(input('Qual letra quer deixar maiuscula: ')).strip()
cont = 0
while contador < tamanho_frase:
    letra = frase[contador]
    if letra in usuario:
        cont += 1
    if letra in usuario:
        nova_string += usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
print(cont)

