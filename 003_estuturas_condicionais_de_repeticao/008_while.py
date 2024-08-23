"""
faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado
"""
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n [0] Sair\n"))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    else:
        print("Obrigado por usar o nosso sistema bancário")

