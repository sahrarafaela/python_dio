"""
- um bloco de código identado e identificado.
Na função temos a possibilidade de ter parametros e ela retorna valores

paramentros: entradas
retornos: saída


programar de forma estruturada


* Nome é para valores não explicitos
*args e **kwargs tupla e dicionario
"""

# assim é uma função em python
def exibir_mensagem():
    print("Olá mundo")


#utilizando paramentros:
def exibir_mensagem_2(nome):
    nome_srt = str(nome).title()
    print(f"olá, {nome_srt}")

#utilizando algumas possibilidades
def exibir_mensagem_3(nome = "Sara"):
    print(f"seja bem vindo(a), {nome.title()}")



#necessário chamar função
exibir_mensagem() 
exibir_mensagem_2("sara")
exibir_mensagem_3()
exibir_mensagem_3("sara")