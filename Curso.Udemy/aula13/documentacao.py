num1 = str(input('Digite um numero: ')).strip()
num2 = str (input('Digite outro numero: ')).strip()

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)

    soma = num1 + num2
    print(soma)
else:
    print('erro')
