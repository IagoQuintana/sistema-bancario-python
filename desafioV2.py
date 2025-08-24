
def depositar(saldo,extrato):
    print("------------- DEPÓSITO -------------")
    deposito = float(input("Informe o valor do depósito!\n"))

    while deposito <= 0:
      print("Valor informado está fora do esperado, o depósito deve ser um valor positivo.")
      deposito = float(input("Informe o valor do depósito!\n"))
        
    saldo += deposito 
    print("Depósito realizado!")
    extrato += f'Depósito:\tR$ {deposito:.2f}\n'
    return saldo,extrato

def sacar(saldo,extrato,numero_saques,limite_saques):
    print("------------- SAQUE -------------")
    saque = float(input("Informe o valor do saque!\n"))

    while saque > 500 or saque <=0 or saque > saldo:
        if saque > 500:
            print("O limite de saque é R$500,00")
        elif saque <= 0:
            print("O valor de saque deve ser maior que R$0,00")
        elif saque > saldo:
            print("Sem saldo suficiente para o saque!")

        saque = float(input("Informe o valor do saque!\n"))
    if numero_saques >= limite_saques:
        print("Limite diário de saques atingido!\n")
    else:           
        numero_saques += 1
        saldo -= saque
        print("Saque realizado!")
        extrato += f'Saque:\t\tR$ {saque:.2f}\n'
    return saldo,extrato,numero_saques

def tirar_extrato(saldo,extrato):
    print("------------- EXTRATO -------------")
    print(extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    
    return saldo, extrato

def main():
    
    menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
            
            """
            
    saldo = 0.00
    limite = 500.00
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    
    while True:

        opcao = input(menu)


        if opcao == 'd':
            saldo,extrato = depositar(saldo,extrato)
                            
        
        elif opcao == 's':
            saldo,extrato,numero_saques = sacar(saldo,extrato,numero_saques,limite_saques)
          
        
        elif opcao == 'e':
            saldo,extrato = tirar_extrato(saldo,extrato)

    
        elif opcao =='q':
            print("Sistema encerrado!")
            break;
    
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == '__main__':
    main()

