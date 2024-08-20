"""
!IMPORTANT:
A documentação deste arquivo será em pt-br e o código em en, para aplicar o conteúdo de inglês estudado no dia e também para fixação.
----------------------------------------
COMO receber e exibir informações para usuário
ler valores com a função input e imprimindo com a função print


A função print tem 4 argumentos opcionais: sep, end, file e flush

O valor atribuido em INPUT é retornado como str e há possibilidade de manipular o tipo de dado

"""

name = input("What's your name? ")
print(name)

age = input("how old are you? ")
age_int = int(age)
print(f"I'm {age_int} years old")
print(name, age_int, end="...\n")
print(name, age_int, sep="#")