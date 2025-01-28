balance = 0
while True:
    print("\n1.check balance\n2.deposit money\n3.withdraw money\n4.exit")
    choice = input("choose an option:")
    if choice == '1':
        print(f"balance: ${balance}")
    elif choice == '2':
        balance += float(input("deposit amount:"))
    elif choice == '3':
        amount = float(input("withdraw amount:"))
        if amount <= balance:
            balance -= amount
        else:
            print("insufficient balance")
    elif choice == '4':
        break
    else:
        print("invalid option")