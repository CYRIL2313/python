#Author:Amal k philip
#Date:14-11-2024
#Description:A number guessing game.The user has to input the starting and ending of th enumber then the program automatically generates a random number whith respect to the starting and ending given by the user.


import random
starting=int(input("Enter the starting"))
ending=int(input("Enter the endding"))
number=random.randint(starting,ending)
no_of_tries=0
while True:
   guess=int(input("Enter your guess"))
   if guess>number:
      print(" GUESS TO HIGH")
      no_of_tries+=1
   elif guess<number:
      print("GUESS TO LOW")
      no_of_tries+=1
   else:
      print("CONGRULATIONS YOUR GUESS IS CORRECT!!!",number)
      print("number of tries:",no_of_tries)