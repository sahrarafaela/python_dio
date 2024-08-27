"""
def f (pos1, pos2, /, pos_or_kwd, *, kwd1, kwd1):
posicao
posicao ou kwarg
palavra

"""

#exemplo:
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234",marca= "Fiat", motor = "1.0", combustivel = "Gasolina")


#extendendo o resultado da função
def sum (a,b):
    return a+b
def subtrair (a,b):
    return a-b

def exibir_resultado (a,b,funcao):
    resultad = funcao(a, b)
    print(f"o resultado da operação é  = {resultad}")

exibir_resultado(10,30, sum)
exibir_resultado(10,30, subtrair)

op = sum
print(op(10,50))


#variavel global e local
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(90))