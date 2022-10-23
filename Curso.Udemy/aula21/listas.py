'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend , + min, max
range


#variavel suporta um unico valor
boleanos = True
inteiros = 10
flutuante = 10.5
strings = 'Textos'

# listas suporta varios valores
#lista = [1, 2, 3, 'texto', True, 10.5]

#indice =  0          1    2    3    4
listas = ['abacate', 'b', 'c', 'd', 'e']

#indice -  3    2    1
print(listas) #mostra lista completa
print(f'{listas[0]} indice {listas.index("abacate")}') #mostra o valor da lista n indice 0 e motra a posicao de abacate
listas[2] = 'banana' #troca o valor na posicao de indice 2 por banana
print(listas)
print(listas[:4])#acessa a lista por fatiamento posicao 0 ate 3
print(listas[3:])#acessa a lista por fatiamento inicio3 ate o final
print(listas[::2])#acessa a lista por fatiamento inicio; fim; passo 2
print(listas[::-1])#acessa a lista por fatiamento invertendo valores na lista


string = 'abcd'
print(string)
print(f'{string[2]} indice {string.index("c")}')

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1,l2)
l3 = l1 + l2 #o + concatena a l1 com l2 e atribui em l3
print(l3)
l1.extend(l2) #l1 concatena o valor dentro de l2 dentro de l1
print(l1)
# ou posso tambem adicionar um elemento com extend exemplo
l3.extend('a')
print(l3)
#podemos adicionar valores ao final da lista com variavel.append('valor a ser adicionaod')
l2.append(7)
print(l2)
#podemos adicionar valores em qualquer indice da lista com variavel.insert(posiicao,'valor a ser adicionaod')
l1.insert(2,'oi')
print(l1)
#podemos deletar um elemento do final da lista sem passar parametro nenhum com
#l1.pop()
l1.pop()
print(l1)

#indice  0  1  2  3  4  5  6  7  8
l2 =    [1, 2, 3, 4, 5, 6, 7, 8, 9]
#para tirar varios valores
del(l2[::2]) #parametro del(variavel[inicio:fim:passo])
print(l2)
del(l2[:2])#parametro del(inicio ate indice 2)
print(l2)
# del pode excluir por fatiamento ou apenas pelo indice
l2.insert(0,'banana')
print(l2)
del(l2[1])
print(l2)

#valor macimo e valor minimo utiliza se max(lista) e min(lista)
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l2), min(l2))

#adicionano valores de forma automatica na lista em range
l2 = list(range(0,100,8)) #list converte objeto iteravel em lista variavel = list(range(inicio,fim,passo))
print(l2)

#listas tambem sao object interaveis podendo ser utilizada com for e while
soma = 0
for valor in l2:
    print(valor, end=' ')
    soma +=valor
print(soma)

#lista com tipos diferntes em sua atribuiçao
lista = ['string', True, 10, 10.4]
#mostra para o usuario o tipo composto de cada elemento na lista str, boolean, int e float
for elemen in lista:
    print(f'O tipo de {elemen} e {type(elemen)}')
'''
# joguinho forca
secreta = 'perfume' #cadastro de palavra
digitada = [] #lista
tentativas = 0
chances = 6

while True:
    if chances < 1:
        print('GAME OVER!!!Voce passou o numero de tentativas')
        break

    #teste digitando letra
    letra = str(input('Digite uma letra: ')).strip()
    #controle de numeros de letras digitadas permitindo so 1 letra
    if len(letra) > 1:
        print('Ahhh!!! Isso não vale digite apenas uma letra.')
        continue
    #armazena letra digitada na lista
    digitada.append(letra)
    #teste se a letra estiver na secreta continua armazenado caso contrario deleta a letra da lista
    if letra in secreta:
        print(f'UHUUUUL, A letra "{letra}" existe na palavra secreta ')
    else:
        print(f'AFFF; A letra "{letra}" nao existe na palavra secreta')
        digitada.pop()
    #inicializa uma palavra vazio para posteriormente ser concatenada
    secreto_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitada:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    print(secreto_temporario)
    if secreto_temporario == secreta:
        tentativas += 1
        print(f'Parabens voce ganhou!!! Voce fez {tentativas} tentativas')
        break
    tentativas += 1
    if letra not in secreta:
        chances -= 1
        print(f'Voce ainda tem {chances} tentativas')


print('>>FIM DE JOGO<<')



