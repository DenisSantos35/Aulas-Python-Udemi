#       [012345678]  indices positivos
texto = 'Python s2'
#      -[987654321]  indices negativos
url = "www.google.com.br/"
print(url[:-1])
print(texto[2])  #acessa o indice 2 do valor armazenado a variavel texto
print(texto[-9]) #acessa o ultimo indice do valor armazenado na variavel texto

nova_string = texto[0::2] #fatiar string primeiro caracter inicio : ultimo caracter final
print(nova_string)
print(len(texto))
numero = -5
print(abs(numero))
