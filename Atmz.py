# ALEX BANK ATM

balance = 20000


def Login(name, password):
    if password == 1234:
        print(f"LOGIN SUCCESSFUL!\nWelcome {name} to Alex Bank PLC.")
        return True
    print("Invalid Credentials")
    return False


def atm(choice, balance):
    if choice == 1:
        print(f"Your current balance is N{balance}")
    elif choice == 2:
        amount = int(input("Enter deposit amount: N"))
        balance += amount
        print(f"Deposit Successful! Your new balance is N{balance}")
    elif choice == 3:
        amount = int(input("How much would you like to withdraw? N"))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Withdrawal successful. Your current balance is N{balance}")
    elif choice == 4:
        print("\nHow much airtime would you like to purchase?")
        print("1. 4GB for N4000")
        print("2. 2GB for N500")
        print("3. 1GB for N100")
        airtime_choice = int(input("Choose an option: "))

        if airtime_choice == 1:
            price = 4000
        elif airtime_choice == 2:
            price = 500
        elif airtime_choice == 3:
            price = 100
        else:
            print("Invalid Option")
            return balance, False

        if price > balance:
            print("Insufficient Balance")
        else:
            balance -= price
            print(f"Airtime purchase successful. Your current balance is N{balance}")
    elif choice == 5:
        print("Thank you for banking with us, see you next time!")
        return balance, True
    else:
        print("Invalid Option")

    return balance, False


name = input("Enter your name: ").strip().title()
password = int(input("Enter your PIN: "))

if Login(name, password):
    while True:
        print("\nWhat would you like to do today?")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Buy Airtime")
        print("5. Exit")
        choice = int(input("Choose an option: "))

        balance, should_exit = atm(choice, balance)
        if should_exit:
            break


if __name__ == "__main__":
    main()

