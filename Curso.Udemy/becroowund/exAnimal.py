#lista com condições
familia = ['vertebrado', 'invertebrado']
tipo = ['ave', 'mamifero', 'inseto', 'anelideo']
especie = ['carnivoro', 'onivoro', 'herbivoro', 'hematofago']
#tratamento de erro
def escreva(familia):
    while True:
        try:
            testeFamilia = str(input()).strip()
        except:
            continue
        else:
            if testeFamilia in familia:
                return testeFamilia
            else:
                continue

#entrada de dados pedido pelo beecrownd
fam = escreva(familia)
tip = escreva(tipo)
esp = escreva(especie)

#condiçoes para resposta com repetição e aninhamento
while 'vertebrado' == fam:
    while 'ave' == tip:
        if 'carnivoro' == esp:
            print('aguia')
        elif 'onivoro' == esp:
            print('pomba')
        break
    while 'mamifero' == tip:
        if 'onivoro' == esp:
            print('homem')
        elif 'herbivoro' == esp:
            print('vaca')
        break
    break

while 'invertebrado' == fam:
    while 'inseto' == tip:
        if 'hematofago' == esp:
            print('pulga')
        elif 'herbivoro' == esp:
            print('largata')
        break
    while 'anelideo' == tip:
        if 'hematofago' == esp:
            print('sanguessuga')
        elif 'onivoro' == esp:
            print('minhoca')
        break
    break


