"""
pode-se usar if dentro de outro if
"""


conta_normal = True
conta_universitaria = False

saldo = 30
saque = 500
cheque_especial = 450


if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
	    print("Saque realizado com uso do cheque especial!")
    # else:
    #     print("saque não realizado")

    
elif conta_universitaria:
	if saldo >= saque:
		print("Saque realizado com sucesso!")
	else:		
		print("Saldo insuficiente!")
