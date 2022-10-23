'''while True:
    try:
        valor = int(input('Digite um numero: '))
    except:
        print('Não é um numero inteiro, Por favor digite um numero inteiro:')
        continue
    else:
        if valor % 2 == 0:
            print(f'O numero {valor} é um numero par.')
            break
        else:
            print(f'O numero {valor} é impar.')
            break'''
numero_inteiro = str(input('Digite um numero inteiro: '))

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print(f'O numero {numero_inteiro} é par.')
    else:
        print(f'O numero {numero_inteiro} é impar.')
else:
    print('isso nao e um numero inteiro!!')

