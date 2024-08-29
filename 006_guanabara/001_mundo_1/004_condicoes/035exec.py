#Desenvolva um programa que leia o comprimanto da três retas a diga ao usuário se elas podem ou não formar um triângulo.

reta_1 = int(input("Qual o tamanho da primeira reta? "))
reta_2 = int(input("Qual o tamanho da segunda reta? "))
reta_3 = int(input("Qual o tamanho da terceira reta? "))


if (reta_1 == reta_2) and (reta_1 == reta_3) and (reta_2 == reta_3):
    print("formou um triangulo")
else:
    print("error")