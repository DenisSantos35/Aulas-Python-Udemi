#fatiamento de string
# 012345678
# Ola mundo
#-987554321
#Fatiamento [i:f:p] [::]
# obs.: a funcao len retorna a quantidade de caracteres da str

variavel = 'Olá mundo'

print(variavel[4::])
print(len(variavel))
variavel = variavel.split(' ');
for valor in variavel :
    print(valor)
