"""
string = cadeia de textos = str
em aspas simples ou dupla
"""

#fatiamento
frase = "Curso em vídeo Python"
#o primeiro numero é o numero exato do index 
#o segundo numero tem que ser 1 a mais do valor que deseja ser retornado

#->incluindo o 9 e removendo o 13
print(frase[9:14])
#start, stop,step
print(frase[9:14:2])
#vai constar a mensagem até o 5 respeitando a regra da exclusão do valor informado
print(frase[:5])

#quero a partir do 15 nesse caso index
print(frase[15:])

#vai do 9 ate o final e o :3 fica como step, pois não informei o valor de stop entao o python conta ate o final da string
print(frase[9::3])