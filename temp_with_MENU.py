#Author:cyril
#date:28/10/2024
#Description:Write a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit.
# The program should repeatedly display a menu with three options:
while True:
    print("MENU\n1.\tCelsius to Fahrenheit")
    print("2.\tFahrenheit to Celsius")
    print("3.\tExit")
    choice=int(input("Enter your choice"))
    if choice == 1:
       tem = float(input("Enter the  in degree per celsius"))
       C=(9/5*tem)+32
       print(tem,"celsius is",C,"fahrenheit")
    elif choice == 2:
       tem = float(input("Enter the temperature in fahrenheit"))
       F=5/9*(tem-32)
       print(tem,"fahernheit is",F,"celsius")
    elif choice == 3:
        break
