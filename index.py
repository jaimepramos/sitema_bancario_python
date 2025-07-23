menu = """
    [1] Deposito
    [2] Saque
    [3] Extrato
    [0] Sair
=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print(' Deposito '.center(40,'#'))
        while True:
            deposito = float(input('Valor: '))
            if deposito > 0:
                extrato += (f'+ R$ {deposito:.2f} \n')
                saldo += deposito
                print('Deposito realizado com sucesso!\n')
                print(f'Saldo Total: R$ {saldo:.2f} \n')

                menu_deposito = ('[1]-Novo Deposito [0]-Home => ')
                opcao_menu_deposito = int(input(menu_deposito))
                if opcao_menu_deposito == 1:
                    continue
                else:
                    break

            else:
                print('Valor de Deposito invalido!')
    elif opcao == 2:
        print(' Saque '.center(40,'#'))
        while True:
            saque = float(input('Valor: '))
            if ((saldo <= 0) or (saldo < saque)):
                print(f'Saldo insuficiente: R$ {saldo:.2f}')
                break
            elif numero_saques >= LIMITE_SAQUES:
                print('Quantidade de Saque diario atingido!')
                break
            elif saque > limite:
                print(f'Valor maior que o limite: R$ {limite:.2f}')
            elif saque <= 0:
                print(f'Valor Invalido para Saque: R$ {saque:.2f}')
            else:
                saldo -= saque
                numero_saques += 1
                extrato += (f'- R$ {saque:.2f} \n')
                print(f'Saque realizado com sucesso: R$ {saque:.2f}, \n')
                print(f'Saldo Total: R$ {saldo:.2f} \n')

                menu_saque = ('[1]-Novo Saque [0]-Home => ')
                opcao_menu_saque = int(input(menu_saque))
                if opcao_menu_saque == 1:
                    continue
                else:
                    break
    elif opcao == 3:
        while True:
            print(' Extrato '.center(40,'#'))
            print('Não houve mevimentação.\n' if not extrato else extrato)
            print(f'Saldo: R$ {saldo:.2f} \n')

            menu_extrato = ('[1]-Novo Extrato [0]-Home =>')
            opcao_menu_extrato = int(input(menu_extrato))
            if opcao_menu_extrato == 1:
                continue
            elif opcao_menu_extrato == 0:
                break
    elif opcao == 0:
        break
    else:
        print('Opção invalida!')

