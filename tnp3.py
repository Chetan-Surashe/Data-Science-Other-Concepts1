# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:01:25 2024

@author: Chetan Surashe
"""
ch="y"
count=0
name=input("Enter your name: ")
while(ch!="n"or count==3):
 import random
 import math
 

 num = random.randint(1, 100)

 choice = random.choice(["square", "square root"])

 if choice == "square":
     print("Tell me the square of", num)
     sq_ans=int(input("Enter your answer: "))
     if sq_ans==num*num:
         print("Congratulations Chetan")
         count=count+1
     else:
         print("OOPS wrong this time!Please try again")
        
    
 elif choice == "square root":
     def is_perfect_square(num):
       sqrt_num = math.sqrt(num)
       return sqrt_num.is_integer()

     def generate_random_square():
        while True:
         random_num = random.randint(1, 100)  # Adjust the range as needed
         if is_perfect_square(random_num):
            return random_num
        print("Tell me the square root of", random_num)
     generate_random_square()
     #print("Tell me the square root of", random_num)
     sqrt_ans=int(input("Enter your answer: "))
     if sqrt_ans==math.sqrt(num):
         print(f"Congratulations {name} ")
     else:
         print("OOPS wrong this time!Please try again")
 ch=input("Do you want to continue...(y/n)")
