"""
Em alguns momentos será necessário converter o tipo de uma variável para manipular de forma diferente.

-> é importante entender que existe uma diferença entre "/" e "//"
-> é possível converter str em int ou float, mas o contrário não é possível

"""
# TIPO FLOAT
preco = 10
print(preco)
# para converter:
preco = float(preco)
print(preco)
# outra forma de mudar é utilizando a multiplicação:
preco = 10 / 5
print(preco)


# TIPO INTEIRO

preco = 10.30
preco = int(preco) #/10

# PARA STRING
preco = 10.50
idade = 28
print(str(preco))
print(str(idade))
texto = f"idade: {idade} preço: {preco}"
print(texto)
