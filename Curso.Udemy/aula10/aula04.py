def loguin(senha, usuario):
    numero = 927401
    pessoa = 'DENIS'
    if senha == numero and pessoa == usuario:
        return 'Loguim efetuado com sucesso'
    else:
        return 'Senha incorreta.'



usuario = str(input('Digite o nome de usuario: ')).strip().upper()
senha = int(input('Digite a senha: '))
print(loguin(senha, usuario))
