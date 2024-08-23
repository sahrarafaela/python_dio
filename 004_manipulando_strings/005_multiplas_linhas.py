"""
string multi linhas

-> ela preserva a formatação do valor inserido
"""

nome = "Guilherme"
mensagem = f"""
Olá meu nome é {nome}, 
Eu estou aprendendo python
"""

mensagem = f'''
Olá meu nome é {nome}, 
Eu estou aprendendo python.
Essa mensagem tem diferentes recuos
'''

print(mensagem)


print(
    """
==========MENU==========
1 - Depositar
2 - Sacar
0 - Sair

===========================
Obrigada por usar nosso sistema!!!
"""
)