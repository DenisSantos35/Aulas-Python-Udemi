salario = float(input())
inteiro = ((salario // 1000)*1000)-2000
print(inteiro)
if salario >=0 and salario <= 2000.00:
    print('Isento')
elif salario >= 2000.01 and salario <=3000.00:
    imposto = 8
elif salario >= 3000.01 and salario < 4500.00:
    imposto = 18
else:
    imposto = 28


