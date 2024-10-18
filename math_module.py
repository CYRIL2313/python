# Author:cyril
# date:18/10/2024
# Description:A Python program that uses functions from the math module to perform the
# following operations on a number provided by the user:
import math
number=int(input("Enter a number:"))
square_root=math.sqrt(number)
print("square root of",number,":",square_root)
math_factorial=math.factorial(number)
print("factorial of",number,":",math_factorial)
math_power=math.pow(number,3)
print("power of",number,":",math_power)