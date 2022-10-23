quantidade = 5
contagem = comtImpar = contPositivo = contNegativo = 0
for cont in range(0,quantidade):
    valores = int(input())
    if valores % 2 == 0:
        contagem += 1
    else:
        comtImpar += 1
    if valores > 0:
        contPositivo += 1
    elif valores < 0:
        contNegativo += 1
print('{} valor(es) par(es)'.format(contagem))
print('{} valor(es) impar(es)'.format(comtImpar))
print('{} valor(es) positivo(s)'.format(contPositivo))
print('{} valor(es) negativo(s)'.format(contNegativo))
