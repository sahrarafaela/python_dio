#Faça um programa que leia o nome completo de uma pessoa. mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza último Souza primeiro Ana

nome = input("Qual o seu nome completo: ")
separando_nome = nome.split()

print(

    f'''
    primeiro nome = {separando_nome[0]}
    ultimo nome = {separando_nome[-1]}
    '''
)
#outra forma de fazer
#  ultimo nome = separando_nome[len(separando_nome)-1]

