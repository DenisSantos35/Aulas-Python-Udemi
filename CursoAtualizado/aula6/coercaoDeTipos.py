'''
conversão de tipos, coersão
type convertion, typecasting, coercion
é o ato  de converter um tipo em outro
tipos imutaveis em primitivos:
str, int, float, bool
'''
#polimorfismo utiliza do mesmo operador para fazer situações diferentes
print(type(1 + 1))
print(type(str(1+1)))
print(type(float(1+1)))
print('a' + 'b')
print(int('1') + 1)
print(bool(0))
print(bool(''))
print(bool(None))
print(bool(bool))

try:
    numero = 10 + 5
    print(numero)
except:
    print('Erro')
finally:
    print('finalizou')
