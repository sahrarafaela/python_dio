#Crie um programa qua leia um número inteiro a mostra na tela se ela é PAR ou IMPAR.

numero = input("Digite um número: ")
int_numero = int(numero)


if int_numero%2 == 0:
    print("PAR DEMAIS")
else:
    print("É IMPAR")