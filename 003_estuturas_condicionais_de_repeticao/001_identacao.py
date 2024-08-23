"""

a limitação de um bloco de código é feita através da identação, pois no python não há caracteres para essa limitação
 
-> é indicado utilizar 4 espaços em branco como boa prática
"""

def sacar (valor: float):
    saldo = 500
    if saldo >= valor:
        print(f"valor de R$ {valor},00  sacado!")

sacar(100)