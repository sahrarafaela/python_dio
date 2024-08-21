"""
retorna um booleano e é utilizado com os operadores de comparação


"""
saldo = 1000
saque = 200
limite = 100

saldo >= saque # >> True
saque <= limite # >> False

#usando operador logico

# no operador E(and) precisa ter todos os valores comparados verdadeiros para retornar True
saldo >= saque and saque <= limite # >> False (operador E)


# no operador OU(or) precisa ter pelo menos um valor comparado verdadeiro para retornar True
saldo >= saque or saque <= limite # >> True (operador ou)


#operador de negação inverte o valor booleano
contatos_emergencia = []
not 1000 > 1500 # >> True (operador de negacao)
not contatos_emergencia # >> True
not "saque 1500;" # >> False
not "" # >> True

#parentese usa-se como na matemática

saldo = 1000
saque = 250
limite = 200
conta_especial = True

# má prática
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque # >> True

#boa prática com parenteses
exp_2 =  (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # >> True

print(exp)
print(exp_2)

#faturando código com boas práticas para um bom entendimento do código
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3) #>> True

