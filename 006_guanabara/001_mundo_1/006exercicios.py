#Cria um algoritmo qua laia um número a mostre o seu dobro. triplo a raiz quadrada.


float_numero = 2

dobro = float_numero * 2
triplo = float_numero * 3
raiz_quadrada = (float_numero ** (1/2))


print(f"o dobro: {dobro:.0f}, o triplo: {triplo:.0f}, a raiz quadrada: {raiz_quadrada:.2f}")



#Dasanvolva um programa que leia as duas notas da um aluno. calcula a mostra a sua média.


nota_1 = 20
nota_2 = 5
media_notas = (nota_1 + nota_2) / 2
print(f"a nota é {media_notas}")


#Escrava um programa que laia um valor am matros ao axiba convertido em centimetros milímetros.

metros = 1

print(f"valor em centimentros: {metros * 100}cm em milimentros {metros * 1000}mm")

#Faça um programa qua laia um número Inteiro qualquer a mostra na tela a sua tabuada.


int_numero = 2

for i in range(1,11):
    print(f"{i} X {int_numero} =  {int_numero * i}")


#Cria um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela poda comprar. Considera US$1.00 = R$3.27


reais  =  800
convertido_em_dolar = reais/3.27
print(f"você tem U${convertido_em_dolar:.2f}")


#Faça um programa que leia a largura a a altura de uma parada am metros. calcula a sua arGa a quantidade de tinta necessária para pintá-la, sabendo que cada litro da tinta. pinta uma área de 2m².


altura = 3
largura = 60
area = (altura * largura) // 2

print(f"vai precisa de {area}L de tinta ")

#Faça um algoritmo qua laia o prašo da um produto a mostre squ novo preço. com 5% da desconto.
preco = 200
desconto = (preco * 0.05)
print(f"o valor do desconto foi R$ {desconto:.0f}")

#Faça um algoritmo qua leia o salário de um funcionário a mostre sau novo salário. com 15% de aumento.

salario = 1600
aumento = (salario * 0.15) + salario
print(f"seu novo salário é R$ {aumento:.2f}")


preco = 123.95
desconto = preco - (preco * 0.05) 
print(f"{desconto:.2f}")



temperatura_c = 32
temperatura_f = (temperatura_c * 9/5) + 32
print(temperatura_f)

#Escrava um programa que pergunte a quantida percorridos por um carro alugado a a quantidade de dias pelos quais ala foi alugado. Calcula o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

dias = 3
km_percorridos = 350

total = (dias * 60) + (km_percorridos * 0.15)
print(total)