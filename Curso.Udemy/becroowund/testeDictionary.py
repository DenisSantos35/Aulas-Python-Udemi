def criaPessoa(nome,sobrenome,idade):
    return {'nome:' f'{nome}','sobrenome:' f'{sobrenome}','idade:' f'{idade}'}
pessoa1 = criaPessoa('Denis','Santos', 31)
print(pessoa1.nome)
