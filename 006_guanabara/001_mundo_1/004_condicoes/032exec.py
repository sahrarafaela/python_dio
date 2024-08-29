#Faça um programa que leia um ano qualquer a mostra se ele é BISSEXTO.

from calendar import isleap
ano = input("Digite um ano qualquer: ")
int_ano = int(ano)


if isleap(int_ano):
    print("É BISSEXTO")
else:
    print("É não")

if((int_ano % 100 == 0) and (int_ano % 4 == 0)):
    print("É BISSEXTO")
else:
    print("É não")