#DasEnvolva um programa que perguntE a distância da uma viagam em Km. Calcule o preço da passagem.cobrando R$0.50 por Km para viagens de até 200Km a R$0.45 para viagens mais longas.

distancia = input("Quanto de distancia tem o destino? ")
int_distancia = int(distancia)

if int_distancia <= 200:
    valor = int_distancia * 0.50
    print(f"você pagará: {valor:.2f}")
    
elif int_distancia > 200:
    valor = int_distancia * 0.45
    print(f"Você pagará {valor:.2f}")