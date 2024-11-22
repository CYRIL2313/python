# AUTHER:CYRIL
# DATE:22/11/2024
# DESCRIPTION:Program to construct patterns of stars (*), using a nested for loop.

row=int(input("enter the rows:"))
for i in range(0,row):
    for j in range(0,i):
        print("*",end=" ")
    print("*")

row2=int(input("enter the rows:"))
for i in range(row2,0,-1):
    for j in range(i-1):
        print("*",end=" ")
    print("*")

row3=int(input("enter the rows:"))
for i in range (1,row3+1):
    for j in range(row3-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print(" ")

row4= int(input("enter the rows:"))
for i in range(row4,0,-1):
    for j in range(row3-i):
            print(" ", end=" ")
    for k in range(2 * i - 1):
            print("*", end=" ")
    print("")





