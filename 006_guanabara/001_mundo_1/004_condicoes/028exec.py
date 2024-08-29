#Escrava um programa que faça o computador "pensar" em um número inteiro antre 0 a 5 a peça para o usuário tentar descobrir qual foi o número escolhido palo computador. O programa devará escrever na tela se o usuário venceu ou perdeu.

import random

numero_usuario = input("Digite um número: ")
numero_aleatorio = random.randrange(1,6)
tratando_numero_usuario = int(numero_usuario)

if numero_aleatorio == tratando_numero_usuario:
    print(f"MEU PARABÉNS, VOCÊ ACERTOU. O NÚMERO É {numero_aleatorio}")
else:
     print(f"NÃO FOI DESSA VEZ... O NÚMERO É {numero_aleatorio}")