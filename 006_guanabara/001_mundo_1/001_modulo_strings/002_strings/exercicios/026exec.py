#Faça um programa que leia uma frase pelo teclado e mostre: 
# Quantas vezes aparece a letra "A". 
# Em que posição ela aparece a primeira VEZ. 
# Em que posição ela aparece a última vez.

frase = input("Digite uma frase legal: ").upper()
contado_a = frase.count("A")
primeiro_a = frase.find("A") + 1

ultimo_a = frase.find("A",-1) +1
#pode se usar o rfind
ultimo_a = frase.find("A",-1) +1
# ultimo_a = frase.rfind("A") +1
print(ultimo_a)
