while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        break


for numero in range(100):
    if numero == "10":
        break
    if numero == "12":
        continue #tira o numero 12 da contagem
    print(numero, end= "*")