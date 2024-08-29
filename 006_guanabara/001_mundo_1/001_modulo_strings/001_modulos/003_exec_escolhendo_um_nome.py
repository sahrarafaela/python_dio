from random import shuffle



#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos a mostra a ordem sortaada.



print("Digite o nome dos alunos ")
aluno_1= input("Primeiro aluno: ")
aluno_2= input("Segundo aluno: ")
aluno_3= input("Terceiro aluno: ")
aluno_4= input("Quarto aluno: ")


lista = [aluno_1, aluno_2, aluno_3, aluno_4]

shuffle(lista)
print(lista)