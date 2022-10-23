from datetime import date
def escrevaNome(msg):
    try:
        nome = str(input(msg)).upper()
        while nome.isnumeric() or nome.isspace():
            nome = str(input(msg)).strip().upper()
    except:
        print('Erro, nome invalido')
    else:
        return nome


def escrevaIdade(msg):
    while True:
        try:
            idade = int(input(msg))
        except:
            print('Erro, digiteum numero valido')
            continue
        else:
            return idade



nome = escrevaNome('Qual o seu nome? ')
idade = escrevaIdade('Qual a sua idade? ')
ano_nascimento = date.today().year - idade
print(f'{nome} tem {idade} anos '
      f'{nome} nasceu em {ano_nascimento}')

