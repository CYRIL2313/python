#Author:cyril
#Date:25-10-2024
#Description: Write a Python program to find the largest of three numbers.
# The program should take three numbers as input from the user and determine which one is the largest.
# Use conditional statements to compare the numbers.
number1=int(input("Enter the first number"))
number2=int(input("Enter the first number"))
number3=int(input("Enter the first number"))
if number1>number2 and number1>number3:
    print("number1 is greater")
elif number2>number1 and number2>number3:
    print("number2 is greater")
elif number3>number2 and number3>number1:
    print("number3 is greater")