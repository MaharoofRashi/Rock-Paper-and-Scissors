import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
whole = rock, paper, scissors

user_entered = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_entered == 0:
  print(rock)
elif user_entered == 1:
  print(paper)
elif user_entered == 2:
  print(scissors)

system_entered = int(random.randint(0,2))
print("Computer chose: ")

if system_entered == 0:
  print(rock)
elif system_entered == 1:
  print(paper)
elif system_entered == 2:
  print(scissors)

if (user_entered == 0) and (system_entered == 2):
  print("You Wins !!!")
elif (user_entered == 2) and (system_entered == 0):
  print("You lose...")
  
elif (user_entered == 2) and (system_entered == 1):
  print("You Wins !!!")
elif (user_entered == 1) and (system_entered == 2):
  print("You lose...")

elif (user_entered == 1) and (system_entered == 0):
  print("You Wins !!!")
elif (user_entered == 0) and (system_entered == 1):
  print("You lose...")
elif (user_entered == system_entered):
  print("Draw")
else:
  print("You have entered an invalid number, you fool !!!")
