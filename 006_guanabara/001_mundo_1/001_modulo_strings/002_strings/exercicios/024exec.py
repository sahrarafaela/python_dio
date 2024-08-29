#Cria um programa qua leia o nome de uma cidade a diga se ela começa ou não com o nome "SANTO".

cidade = input("qual o nome da sua cidade? ").upper()
fatiando_cidade = cidade.split()
procurando_santo = "SANTO" in fatiando_cidade[0]

print(procurando_santo)