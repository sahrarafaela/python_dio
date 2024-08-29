#Escreva um programa qua leia a velocidade de um carro.   Se ele ultrapassar 80km/h,mostra uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada Km acima do limita.


velocidade = 900
if velocidade > 80:
    multa = (velocidade - 80) *  7
    print(f"você ultapassou o limite e terá que pagar {multa:.0f},00 reais")