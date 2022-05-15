def atm():
    pin = input("Enter your PIN : ")
    if pin == "1234":
        print("Login Success...")
    else:
        # print("Login Failed...")
        raise ValueError("Login Failed...")

    totalBal = 10000
    amount = int(input("Enter amount you want to withdraw : "))
    if amount > totalBal:
        # print("Insufficient Balance...")
        raise ValueError("Insufficient Balance")
    else:
        totalBal -= amount
        print("Transaction Successfull...")
        print("Remaining Balance is :",totalBal)

try:
    atm()
except ValueError as msg:
    print(msg)