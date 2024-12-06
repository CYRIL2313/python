#Author:cyril
#date:18/10/2024
#Description:PROGRAM TO FIND THE FACTORIAL OF A NUMBER USING RECURSION

def factorial(n):
    if n==0:
        return 1
    else:
         return  n*(factorial(n-1))
n=int(input("Enter The number"))
f=factorial(n)
print("The factorial of",n,"is",f)
