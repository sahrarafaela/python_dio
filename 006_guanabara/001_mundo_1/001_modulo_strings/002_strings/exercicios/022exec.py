#Crie um programa que leia o nome completo de uma pessoa e mostra: 
# O nome com todas as letras maiúsculas 
# O nome com todas minúsculas. 
# Quantas letras ao todo (sem considerar aspaços). 
# Quantas letras tem o primeiro nome.

nome_completo = "Sara Rafaela Nascimento"
nome_tratado = str(nome_completo)

#exibindo nome em letras maiúsculas 
nome_maiusculo = nome_tratado.upper()

#exibindo nome em letras minúsculas 
nome_minusculo = nome_tratado.lower()

#quantas letras ao todo sem considerar aspaços
separando_letras = nome_tratado.split()
tratando_letras = "".join(separando_letras)
contando_letras = len(tratando_letras)

#Quantas letras tem o primeiro nome
lista_nome = nome_completo.split()
retornando_nome = lista_nome[0]


#resolução guanabara

nome = str(input('Digite seu nome complete: ')).strip()
               
print('Analisando seu nome...') 
print('Seu nome em maiúsculas é {}'.format(nome.upper()))

print('Seu nome em minúsculas é {}'.format(nome.lower())) 

print('Seu nome tem ao todo tem {} letras'.format(len(nome) - nome.count(" ")))

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split() 
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len (separa [0])))