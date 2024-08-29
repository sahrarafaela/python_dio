#Cria um programa qua laia um número Real qualquer palo teclado a mostra na tala a sua porção Inteira.
import math
import random
# from  math import  trunc

num = 6.99
# num_tratado = math.trunc(num)
num_tratado = math.trunc(num)
print(num_tratado)

#Faça um programa que leia o comprimento do catato oposto a do cateto adjacenta de um triângulo ratângulo, calcula a mostre o comprimanto da hipotanusa.
cateto_1 = 2
cateto_2 = 2.5
hipotenusa = math.sqrt((cateto_1 ** 2) + (cateto_2 ** 2))
print(f"{hipotenusa:.2f}")
#exemplo utilizado pelo guanabara:
h = math.hypot(cateto_1, cateto_2)
print(f"{h:.2f}")


#Faça um programa qua laia um ângulo qualquer a mostra na tala o valor do sano, cossano a tanganta dessa ângulo.
angulo = 30
seno = math.sin(math.radians( angulo))
cosseno = math.cos(math.radians( angulo))
tangente = math.tan(math.radians( angulo))

print(f"""
    o seno é {seno:.2f}
    o cosseno {cosseno:.2f}
    a tangente {tangente:.2f}
""")

#sem math:
print(f"""
    o seno é {cateto_1 / h}
    o cosseno {cateto_2 / h}
    a tangente {cateto_1 / cateto_2}
""")




#Um professor quar sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ala. lando o noma dalas a ascravando o nome do ascolhido.


print("Digite o nome dos alunos ")
aluno_1= input("Primeiro aluno: ")
aluno_2= input("Segundo aluno: ")
aluno_3= input("Terceiro aluno: ")
aluno_4= input("Quarto aluno: ")


lista = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = random.choice(lista)
print(f"o aluno escolhido foi {escolhido.title()}")
