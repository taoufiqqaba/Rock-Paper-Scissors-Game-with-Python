import os
os.system('cls' if os.name == 'nt' else 'clear')

# Day 4
# import random

# random_int = random.randint( 1,  10 )
# print(random_int)

# random_float = random.random() * 10
# print(random_float)

# random_float = random.uniform(0, 10)
# print(random_float)

# random_heads_or_tails = random.randint (0, 1)
# if random_heads_or_tails == 0:
#     print("heads")
# else: 
#     print("tails")

# Lists

# Musical_Instrument = ["Guitar", "Piano", "Violin"]

# Musical_Instrument.append("Cello")

# print(Musical_Instrument[1])   

# import random

# friends = ["Taoufiq", "Imane", "Houda", "Salima"]
# print(random.choice(friends))

# Rock Paper Scissors Game
import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]

user_choice = int(input("Type 0 for rock 1 for Paper and 2 for Scissors:\n"))

if user_choice >= 3 or user_choice < 0:
    print("You Entered an Invalid Number!. Try Again!")
else:
    print(game_images[user_choice])


computer_choice = random.randint(0, 2)
print("Computer Choose: ")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You Win")
elif computer_choice > user_choice:
    print("You Lose")
elif computer_choice == user_choice:
    print("it's a Draw")
elif computer_choice == 1 and user_choice == 2:
    print("You Win")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose")