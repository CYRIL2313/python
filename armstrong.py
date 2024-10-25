Author:cyril
#date:18/10/2024
#Description:to see if the number amrstrong number
num=int(input("enter the number"))
sum=0
while num>0:
    reminder = num%10
    sum=sum+(reminder**3)
    num = num//10
print("sum of the given digits id",sum)
