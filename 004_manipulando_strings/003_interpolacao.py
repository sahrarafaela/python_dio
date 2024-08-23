"""
% (não utilizada atualmente)
format
f string (mais recomendado)
"""
#%
nome = "Guilherme"
idade = 25
profissao = "Programador"
linguagem = "Python"

mensagem = "Olá, me chamo %s, tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem)

#format
mensagem = "Olá, me chamo {}, tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem)

#outra forma de usar o format
mensagem = "Olá, me chamo {0}, tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguagem)


#outra forma de usar o format
mensagem = "Olá, me chamo {nome}, tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem)


pessoa = {
    "nome": "Guilherme",
    "idade": 28
}
#outra forma de usar o format
mensagem = "Olá, me chamo {nome}, tenho {idade} anos de idade.".format(**pessoa)



#f string o método mais utilizado atualmente
mensagem = f"Olá, me chamo {nome}, tenho {idade} anos de idade, trabalho como {profissao.lower()} e estou matriculado no curso de {linguagem.lower()}."


#formatando strings
PI = 3.14159
novo_valor = f"Valor de PI: {PI:.2f}"  
novo_valor = f"Valor de PI: {PI:10.2f}" #>> adicionar caracteres  
print(novo_valor)