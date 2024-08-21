"""
o que são e como utilizar

são usados para definir valores ou trocar valores

são eles o:
* = atribuição simples
ex: saldo = 500
* += atribuição com adição
ex: saldo += 200 >> 700
* -= atribuição com subtração
ex: saldo -= 200 >> 500
* /= atribuição com divisao
ex: saldo /= 5 >> 100.0
ex: saldo //= 5 >> 100 (divisao inteira)
*%= atribuição com modulo
ex:
saldo = 500
saldo % 480
>> 20
* **= atribuição com exponeciação
ex:
saldo = 80
saldo **= 2
>> 6400

exemplos com código:
"""
print("atribuicao")
saldo = 500
print (saldo)
saldo = 200
print (saldo)

print("outros exemplos")
saldo += 10
print(saldo)

saldo -= 5
print(saldo)

saldo //= 2
print(saldo)


saldo /= 2
print(saldo)


saldo *= 10
print(saldo)

saldo %= 4
print(saldo)

saldo **= 2
print(saldo)
