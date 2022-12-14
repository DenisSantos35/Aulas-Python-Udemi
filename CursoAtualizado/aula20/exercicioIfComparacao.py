primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')
num1 = int(primeiro_valor)
num2 = int(segundo_valor)
if num1 > num2:
    print(f'{primeiro_valor=} e maior que o {segundo_valor=}')
elif num1 < num2 :
    print(f'{segundo_valor=} e maior que o {primeiro_valor=}')
else:
    print(f'{segundo_valor=} e igual ao {primeiro_valor=}')

