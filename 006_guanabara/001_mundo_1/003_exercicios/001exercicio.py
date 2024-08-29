nome = input("Qual o seu nome? ")
sexo = input("Digite [M] para mulher e [H] para homem: ")
convertido_sexo = sexo.lower()

if (convertido_sexo == "m"):
    print(f"Seja bem-vinda {nome.title()}. É um prazer te conhecer")
elif (convertido_sexo == "h"):
    print(f"seja bem vindo {nome.title()}. É um prazer te conhecer")
else:
    print("Digite M ou H, por favor")
    