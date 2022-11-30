"""docStrng
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str ~> string ~> texto
strings são textos que estão dentro de aspas
"""
print(type(1234)) #<class 'int'>
#Aspas Simples
print('Denis Santos', type('')) #Denis Santos <class 'str'>

#Aspas duplas
print("Denis Santos", type("")) #Denis Santos <class 'str'>
print("Denis\ 'Santos'") #Denis\ 'Santos'
#Escape
print("Denis \"Santos\"") #escape utiliza \ para pular o procimo caractere Denis "Santos"

#r
print(r"Denis \"Santos\"") #se queiser que o escape apareca utiliza r para pular o procimo caractere Denis \"Santos\"