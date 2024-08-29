frase = "Curso em vídeo Python"
#verficar o tamanho da str
len(frase)

#contar quantos valores determinados tem dentro de uma str
contando_letras = frase.count('o')
#começa a partir de 0 e termina em 13 -1
contando_letras = frase.count('o', 0, 13)

#quantas vezes ele encontrou:
#quando não encontra, ele retorna um -1
frase.find('deo')

#operador in e retorna um bool
'curso' in frase

