"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, + min, max, range
"""
#acessando indices de lista
"""
variaveis = 'coloca valor na memoria'
print(variaveis)
#         0    1    2    3    4
lista = ['abacate', 'banana', 'caqui', 'damasco', 'escarola', 'acerola']
#    -    5    4    3    2    1
print(lista[::-1]) # :: do fim ate o inicio começando do ultimo elemento
#print(lista[::2]) # :: do inicio ate o fim; 2 pulando de 2 em 2 inicio:fim:passo
#print(lista[:4]) # de 0 ate 4
#print(lista[1::2]) # de 1 ate o final pulando de 2 em 2
#lista[5] = 'Abacaxi'
#string = 'abcde'
#print(string[1])
#print(lista[5], lista)
"""
#adicionando valores e concatenando listas
"""
l1= [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2 #concatena as duas listas
l2.extend(l1) # comando extend tambem concatena extendendo uma lista dentro da outra ou coloca item ao final da lista
            #variavel.extend(variavel ou valor)
l2.append('a') #variavel.append(valor) inseri novo valor ao final da lista
l2.insert(3, 'b') #variavel.insert(indice,valor), insere o valor na posição desejada
print(l1, l2) #imprime as duas listas na tela
print(l3) #imprime em l3 as listas l1 e l2 concatenadas
"""
#deletando valores das listas
"""
l1 = ['denis', 'maria', 'joyce']
print(l1)

l1.pop() #variavel.pop() remove o ultimo valor da lista
print(l1)
#     0  1  2  3  4  5  6  7  8 indices
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)
del(l2[2:5]) #del(lista[indices]) exclui da lista os valores desejados
print(l2)
l2.insert(3, 'banana')
print(l2)
del(l2[3])
print(l2)
"""

#Valores maximo e minimo (max and Min) e iteraçao de lista em for
'''
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l2)) # exibe o valor maximo da lista
print(min(l2)) # exibe o valor minimo da lista
l3 = list(range(1,100)) # o list funcao biutim faz com que fique iteravel o range
    #no caso acima vai atribuir os numero de 1 ate 9 no l3
l4 = list(range(1, 50, 2)) #list(range(inicio,fim,passo))
print(max(l3))

for valor in l3: #valor recebe cada elemento de l3 e fica relaizando o lup ate receber o ultimo valor
    if valor % 10 == 0: #se o valor for divisivel por 10
        print() #pula 1 linha
        print(valor, end='') #imprime o valor concatenando na mesma linha
    else:
        print(valor, end='') #imprime o valor concatenando na mesma linha

l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9] #soma = 45
soma = 0 #inicialização da soma em 0
for valor in l5:
    soma = soma + valor
print(soma)

l6 = ['string', True, 10, -20.6]
for checar in l6:
    print(f'O tipo de {checar} e {type(checar)}')
'''
#criando jogo com lista

secreto = 'perfume'
dados = []
chances = 3
while True:

    if chances <= 0:
        print(f'Você perdeu')
        break
    letra = str(input('Digite uma letra:')) # variavel letra recebe um valor digitado pelo usuario
    if len(letra) > 1: #checa se o usuario digitou mais de uma letra comparando o numero de caracter digitado
        print('Ahhh isso não vale. Digite apenas uma letra.')
        continue #toda vez que encontra essapalavra contnue nao executa nada abaixo e retorna para o laço
    dados.append(letra) #adiciona a letra digitada dentro da lista dados
    if letra in secreto: #se a letra digita for igual alguma palavra dentro da secreta
        print(f'UHUUUUL a letra "{letra}" existe na plavra secreta.')

    else:
        print(f'AFFFFF, A letra não existe "{letra}" na palavra secreta')
        dados.pop() #ou dados.pop()
    print(dados)

    secretoTemporario = ''
    for letraSecreta in secreto: #pega palavra no caso perfume e passa letra por letra
        if letraSecreta in dados: #se a letra digitada for igual a letra secreta no momento armazena e concatena
            secretoTemporario += letraSecreta
        else:
            secretoTemporario += '*' #se nao for igual armazena o asterisco e concatena
    if secretoTemporario == secreto: #se acaso o usuario digitou todas as letras certas compara com palavra secreta
        print('Parabens... Você adivinhou a palavra sevreta')
        print(f'A palavra secreta é {secretoTemporario}')
        break
    else: #caso nao terminou todas as palavras vai mostrando a palavra como esta
        print(f'A palavra secreta está assim {secretoTemporario}')
    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} tentativas')
print(f'>>FIM de jogo <<')























