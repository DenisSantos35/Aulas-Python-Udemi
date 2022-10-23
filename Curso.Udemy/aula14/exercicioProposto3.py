usuario = str(input('Digite seu primeiro nome:' )).strip()
tamanho = len(usuario)
while usuario.isnumeric():
    usuario = str(input('Digite seu primeiro nome:' ))
    tamanho = len(usuario)

if tamanho <= 4:
    print('Seu nome é curto!!!')
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')



