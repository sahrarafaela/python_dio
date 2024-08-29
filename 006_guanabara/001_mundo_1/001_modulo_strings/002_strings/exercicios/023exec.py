#Faça um programa que leia um número de 0 a 9999 mostre na tela cada um dos digitos separados. Ex: Digita um número: 1834 unidade: 4 dezena: 3 centenas: 8 milhar: 1

numero = input("digite um número: ")


msg = f"""

unidade: {numero[3:4]} 
dezena: {numero[2:3]} 
centenas: {numero[1:2]} 
milhar: {numero[0:1]} 

"""
print(msg)