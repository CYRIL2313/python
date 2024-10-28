#Author:cyril
#date:28/10/2024
#Description:Write a program that simulates a simple bank ATM system.
# The user has an initial balance of $1000.
# The ATM should display a menu with options to:
balance_amount=1000
while True:
     print("MENU\n1.\tCheck balance")
     print("2.\tDeposit Money")
     print("3.\tWithdraw Money")
     print("4.\tExit")
     choice=int(input("Enter your choice:"))
     if choice==1:
         print(f"Your balance is ${balance_amount}")
     elif choice==2:
         deposit_amount=float(input("Enter the amount you want to deposit"))
         balance_amount=deposit_amount+balance_amount
         print(f"The amount you have deposited ${deposit_amount} "and
                f"Your balance is ${balance_amount}")
     elif choice==3:
         withdrawel_amount=float(input("Enter the amount"))
         if withdrawel_amount>balance_amount:
             print("insuficient amount")
         elif choice==3:
             balance_amount=balance_amount-withdrawel_amount
             print(f"The amount you have withdrawen ${withdrawel_amount}"and
               f"Your balance is ${balance_amount}")

     elif choice==4:
         break

