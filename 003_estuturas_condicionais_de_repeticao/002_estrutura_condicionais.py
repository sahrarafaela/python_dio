"""
if
if/else
if/elif/else

 
"""

saldo = 2000.0
saque = float(input("Qual o valor do saque: "))

if saldo >= saque:
    ...
   #print("Saque realizado")
if saldo < saque:
    ...
   #print("Saldo insuficiente")


if saldo >= saque:
    ...
   #print("Saque realizado")
else:
    ...
   #print("Saldo insuficiente")



if saldo >= saque:
    ...
   #print("Saque realizado")
else:
    ...
   #print("Saldo insuficiente")

opcao = int (input("Informe uma opção \n[1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo extrato...")
else:
    sys.exit("Opção inválida")