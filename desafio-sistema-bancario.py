
menu = """\n

    "================================ BANCO EXPERIENCE ================================"\n

    "============ CARO CLIENTE,SEJA BEM-VINDO(A) AO NOSSO SISTEMA BANCÁRIO ============"\n

    ================== MENU ================== 

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    =>"""

saldo = 0
limite = 800
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3


while True:
        
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else: 
            print("Operação Falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:  "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
            
        excedeu_saques = numero_saques == LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite")
            
        elif excedeu_saques:
            print("Operação faalhou! Número máximo de saques excedido")
        
        elif saldo > valor:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
                
        else: 
            print("Operação Falhou! O valor informado é inválido.")


    elif opcao == "e":

        print("\n==================EXTRATO==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
        print("============================================")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")