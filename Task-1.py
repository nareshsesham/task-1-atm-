import time
print("please insert your card")
time.sleep(5)
password=1234
pin=int(input("enter your atm pin"))
balance =5000
if pin==password:
    while True:
        print("""
         1 ==balance
         2 ==withdraw balance
         3 ==deposit balance
         4 ==exit
         """)
        try:
            option=int(input("please enter your choice"))
        except:
            print("please enter valid option")
        if option ==1:
            print(f"your Current balance is {balance}")
        if option ==2:
            withdraw_amount=int(input("please enter withdraw amount"))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your acount")
            print(f"your current balance is {balance}")
        if option ==3:
            deposited_amount=int(input("please enter deposit amount"))
            balance=balance+deposited_amount
            print(f"{deposited_amount} is credited to your acount")
            print(f"your updated balance is {balance}")
        if option ==4:
            break
        
    else:
        print("please enter correct pin")
