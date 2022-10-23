ddd = [61, 71, 11, 21, 32, 19,27, 31]
cidade = ['Brasilia', 'Salvador','Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas','Vitoria', 'Belo Horizonte']
dddCidade = int(input())
if dddCidade in ddd:
    posicao = ddd.index(dddCidade)
    print('{}'.format(cidade[posicao]))
else:
    print('DDD nao cadastrado')

