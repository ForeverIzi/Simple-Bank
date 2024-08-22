menu = """

[D] -> Depositar
[S] -> Sacar
[E] -> Extrato
[Q] -> Sair

"""

balance = 0
limit = 500
extract = ""
num_withdraw = 0
WITHDRAW_LIMIT = 3

while True:

    option = input(menu)

    if option == 'd' or option == 'D':
        value = float(input("Informe o valor do depósito: "))

        if value > 0:
            balance += value
            extract += f"Depósito: R$ {value:.2f}\n"
        
    elif option == 's' or option == 'S':

        value = float(input("Informe a quantidade que deseja sacar: "))
        balance_exceeded = value > balance
        limit_exceeded = value > limit
        withdraw_exceeded = num_withdraw > WITHDRAW_LIMIT

        if balance_exceeded:
            print("Falha na operação! Você não tem saldo suficiente.")
        
        elif limit_exceeded:
            print("Falha na operação! O valor do saque excede o limite.")
        
        elif withdraw_exceeded:
            print("Falha na operação! O número máximo de saques já foi efetuado.")

        elif value > 0:
            balance -= value           
            extract += f"Saque: R$  {value:.2f}\n"
            num_withdraw += 1

        else:
            print("Falha na operação! O valor informado não é válido.")

    elif option == "e" or option == "E":
        print("\n====== Extrato ======\n")
        print("Não foram efetuadas movimentações." if not extract else extract)
        print(f"\nSaldo: R$ {balance:.2f}")
        print("\n=====================")
    
    elif option == "q" or option =="Q":
        break
    
    else:
        print("Operação inválida, insira uma opção válida")



