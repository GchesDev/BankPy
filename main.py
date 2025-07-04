
show_menu = """

  1 - Deposit
  2 - Withdraw
  3 - Balance
  4 - Exit

=> """

# Variáveis imutáveis
LIMIT = 500
WITHDRAW_LIMIT = 3

# Variáveis mutáveis
balance = 0
bank_withdrawal = 0
extract = ""

while True:

  option = input(show_menu)

  if option == '1':
    value = float(input("Digite o valor que deseja depositar: "))

    if value > 0:
      balance += value
      extract += f"Depósito de ${value:.2f} efetuado com sucesso."
    else:
      print("Erro de operação, o valor informado não é um float.")
      print("Tente novamente.")
    
  elif option == '2':
    value = float(input("Digite o valor que deseja sacar: "))
    exceeded_balance = value > balance
    exceeded_limit = value > LIMIT
    exceeded_withdrawn = bank_withdrawal >= WITHDRAW_LIMIT

    if exceeded_balance:
      print("Sem saldo suficiente")
    elif exceeded_limit:
      print("O valor excede seu limite!")
    elif exceeded_withdrawn:
      print("Numero máximo de saques!")
    elif value > 0:
      balance -= value
      extract += f"saque de ${value:.2f}"
      bank_withdrawal += 1

    else:
      print("Erro no valor informado, tente novamente.")   
  
  elif option == '3':
    print('-'*50)
    print("Sem movimentações" if not extract else extract)
    print("Balance: ${}".format(balance))
    print('-'*50)

  elif option == '4':
    break

  else:
    print("Erro, opção inexistente. Tente novamente.")




    
                

