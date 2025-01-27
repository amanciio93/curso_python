""" 
    CONSTANTE = "Variáveis" que não vão mudar
        * Muitas condições no mesmo IF é RUIM!
        * Contagem de complexidade é RUIM! - Sublocos demais.
"""

velocidade = 61 # velocidade atual do carro
local_carro = 99 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_acima_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_acima_radar_1

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if velocidade_acima_radar_1:
    print('Velocidade do carro acima do radar 1')

if carro_multado_radar_1:
    print('Carro multado no radar 1')