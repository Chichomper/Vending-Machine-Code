# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:16:55 2025

@author: luiaq
"""

print ("Vending Machine")


print("""   _______________________
  | Drinks :D             |
  |coke 3.50              |
  |vanilla 4.25           |
  |cherry 4.50            |
  |Fanta 5.25             |
  |Sprite 5.50            |
  |Sprite Cranberry 12.25 |
  |Fanta Strawberry 4.50  |
  |Fanta Apple 3.25       |
  |Prime 10.50            |
  |Gatorade 10.25         |
  |Chemical X 0.25        |
  |_______________________|""")
   

#This is an Array for Categorising Drinks, with the use of the the array to categorise the drinks
Drinks ={
1:["Coke", 3.50],
2:["Vanilla Coke", 4.25],
3:["Cherry Coke", 4.50],
4:["Fanta", 5.25],
5:["Sprite", 5.50],
6:["Water", 10],
7:["Sprite Cranberry", 12.25],
8:["Fanta Strawberry", 4.50],
9:["Fanta Apple", 3.25],
10:["Prime", 10.50],
11:["Gatorade", 10.25],
12:["Chemical X", 0.25] 
} 

#This one is justfor finding out how much money you have
Money = float(input("How much Money you got?:"))

#This is using a while loop, for finding the drink you want, but it has a fail safe if incase what you entered is a word
while True: 
    try:numD = int(input("Please enter a Drink(Prices):"))
    except:
        print ("Thats not an Option, please re-enter the correct number.")
        continue
    #This is for checking if the number thats been entered is out of range
    if numD <1 or numD >12:
        print ("Enter a digit between 1-12:")
        continue
    else:
        break
#this one is just basic maths in use for getting the change of the user
for d in Drinks.keys():
    Change = Money - Drinks.get(d)[1]
    if numD == d:
        print(f"Enjoy yourself a {Drinks.get(d)[0]} with a price of ${Drinks.get(d)[1]}")
        print(f"Your change is {Change}")
        break
    
    
 