RADAR_1 = 60 # sinaliza uma constante(não muda)
LOCAL_1 = 100 #local do radar 1 de velocidade 60
RADAR_RANGE = 1

velocidade = 61
local_carro = 99

dentro_range = local_carro >= LOCAL_1 - RADAR_RANGE and local_carro <= LOCAL_1 + RADAR_RANGE
velocidade_acima = velocidade > RADAR_1

if dentro_range:
    if velocidade_acima:
        print('Levou multa')
    else:
        print('não levou multa')
else:
    print('carro está fora do range')

