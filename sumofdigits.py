#Author:cyril
#date:18/10/2024
#Description:program to find sum of the given digits
num=int(input("enter the number"))
sum=0
while num>0:
    reminder = num%10
    sum=sum+reminder
    num = num//10
print("sum of the given digits id",sum)
