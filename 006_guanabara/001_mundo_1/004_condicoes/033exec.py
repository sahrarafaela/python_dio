#Faça um programa qua leia três números a mostre qual é o maior a qual é o menor.

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))
numero_3 = int(input("Digite um número: "))

if (numero_1 > numero_2) and (numero_1 > numero_3):
    print(f"O maior número é {numero_1}")
elif (numero_2 > numero_1) and (numero_2 > numero_3):
    print(f"O maior número é {numero_2}")
else:
    print(f"O maior número é {numero_3}")