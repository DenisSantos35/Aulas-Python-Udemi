#Operadors logicos
#and(e) or(ou) not(nao)
#and - todas as condiçoes precisam ser verdadeiras
#Se qualquer valor for considerado falso, a expressão inteira
#será avaliada naquele valor
#sao consideradas Falsy(que voce ja viu)
#0 0.0 '' False
#tambem existe o tpo None que é 
#usado para representar um nao valor
'''
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')

senha_permitida = '123456'
#if == true:
#  executa o codigo
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
'''

#Avaliação de curto circuito
print(True and '' and True)