#Cria um programa que leia o nome da uma pessoa a diga se ela tem "SILVA" no nome.

nome_completo = input("Qual o seu nome completo? ").upper()
tem_silva = "SILVA" in nome_completo
print(tem_silva)