"""
CONSTANTE = "Variaveis que não vão mudar
Muitas condições no mesmo if(ruim)
   <- contagem de complexidade (ruim)
"""

velocidade = 61 #velocidade atual do carro
local_carro = 99 #local em que o carro está na estrada

RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 esta
RADAR_RANGE = 1 #A distancia onde o radar pega

'''
Sempre tente separar condições em variaves para que if fique mais limpo possivel.
'''
velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro <= (LOCAL_1 + RADAR_RANGE) and \
    local_carro >= (LOCAL_1 - RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1


if velocidade_carro_passou_radar_1 :
    print(f'Carro esta acima da velocidade do Radar')
else:
    print(f'Carro esta abaixo da velocidade do Radar')

if carro_passou_radar_1:
    print('O carro esta no radar 1')

if carro_multado_radar_1:
    print('Carro foi multado')