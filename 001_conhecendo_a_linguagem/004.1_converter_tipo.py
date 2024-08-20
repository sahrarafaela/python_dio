print(int (1.0)) #1
print(int (1.9)) #1
print(int (1.95646564)) #1

print(int("10")) #10
# print(int("10.6")) não é permitido, tem que usar float
print(float("10.6")) #10.6
print(float("10")) #esse é permitido mesmo que esteja usando int retorno 10.0



numero = "10.10"
numero_float = float(numero)
print(numero)
print(type(numero) )
print(type(numero_float) )


print(100/2) #retorna um float
print(100//2) #retorna um inteiro