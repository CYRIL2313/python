#Author:cyril
#date:18/10/2024
#Description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit.
# The user should be able to input a temperature in Celsius or Fahrenheit
# , and the program should convert it to the other unit using the formula:
tem=int(input("Enter the temperature"))
temp_coff=input("Is this in (C)elsius or (F)ahrenheit?")
if temp_coff=="c" or temp_coff=="C":
    C=(9/5*tem)+32
    print(tem,"celsius is",C,"fahrenheit")
elif temp_coff=="f" or temp_coff=="F":
    F=5/9*(tem-32)
    print(tem,"fahernheit is",F,"celsius")


