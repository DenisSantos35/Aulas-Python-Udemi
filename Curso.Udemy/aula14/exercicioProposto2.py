'''def testeHorario(horas):
    while True:
        try:
            h = int(input(horas))
        except:
            print('Formato de horario invalido, digite um horario entre 0h e 23h')
            continue
        else:
            if h >= 0 and h <= 23:
                return h
            else:
                print('Formato de horario invalido, digite um horario entre 0h e 23h')
                continue



horas = testeHorario('Digite quantas horas são: ')
if horas >= 0 and horas <= 11:
    print('Bom Dia!!!')
elif horas >= 12 and horas <= 17:
    print('Boa Tarde!!!')
else:
    print('Boa Noite')'''

horas = str(input('Digite o horario (0-23): '))

if horas.isdigit():
    horas = int(horas)
    if horas < 0 or horas > 23:
        print('O horario deve estar entre 0h e 23h!!!')
    else:
        if 0 <= horas <= 11:
            print('Bom Dia!!!')
        elif horas <=17:
            print('Boa Tarde!!!')
        else:
            print('Boa Noite!!!')
    pass
else:
    print('Nao e um horario valido')
