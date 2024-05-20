saldo = 1500
num_saques = 0
extrato = []

menu_banco = '''
    ( 0 ) - Ver Saldo.
    ( 1 ) - Realizar um saque.
    ( 2 ) - Realizar um depósito.
    ( 3 ) - Mostrar Extrato.
    ( 4 ) - Sair.
'''

while True:
    menu = input("Mostrar Menu: (s/n): ")
    if menu.lower() == 's':
        print(menu_banco)
    option = int(input("Escolha uma opção: "))

    if option == 0:
        print(f"Saldo em conta: R$ {saldo:.2f}")

    elif option == 1:
        saque = float(input("Quanto deseja sacar: "))
        if saque > saldo:
            print("Saque ultrapassa seu saldo atual!")
            print(f"Saldo em conta: R$ {saldo:.2f}")
        elif saque > 500:
            print("Limite máximo de saque permitido: R$ 500,00")
        else:
            if num_saques >= 3:
                print("Limite de saque diário atingido, tente amanhã!")
            else:
                saldo -= saque
                extrato.append(f"Saque: -R$ {saque:.2f}")
                print(f"Saque de R$ {saque:.2f} efetuado com sucesso!")
                num_saques += 1

    elif option == 2:
        deposito = float(input("Quanto deseja depositar: "))
        if deposito <= 0:
            print("Depósito inválido! Valor deve ser maior que R$ 0.00")
        else:
            saldo += deposito
            extrato.append(f"Depósito: +R$ {deposito:.2f}")
            print(f"Depósito de R$ {deposito:.2f} efetuado com sucesso!")

    elif option == 3:
        if not extrato:
            print("Extrato vazio.")
        else:
            print("Extrato:")
            for linha in extrato:
                print(linha)
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif option == 4:
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")