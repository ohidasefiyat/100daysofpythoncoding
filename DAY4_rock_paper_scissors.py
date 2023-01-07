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


# possible choice
possible_choice = [rock, paper, scissors]
# print(possible_choice[0])

# get the user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

# use random function to generate the computer choice
computer_choice = random.randint(0, len(possible_choice)-1)
# print(computer_choice)

if user_choice == computer_choice:
  if user_choice == 0:
    print(f"You both chose: {possible_choice[0]} it's a draw")
  elif user_choice == 1:
    print(f"You both chose: {possible_choice[1]} it's a draw")
  else:
     print(f"You both chose: {possible_choice[2]} it's a draw")
  
elif user_choice == 0:
  if computer_choice == 2:
    print(f"You chose:\n {possible_choice[0]}\nComputer chose: \n{possible_choice[2]}\n Rock wins against scissors, Congratulations you win!")
  else:
     print(f"You chose:\n {possible_choice[0]}\nComputer chose: \n{possible_choice[1]}\nPaper wins against rock, You lose")

elif user_choice == 2:
  if computer_choice == 1:
    print(f"You chose:\n {possible_choice[2]}\nComputer chose: \n{possible_choice[1]}\nscissors wins against a paper,  Congratulations you win!")
  else:
     print(f"You chose:\n {possible_choice[2]}\nComputer chose: \n{possible_choice[0]}\nrock wins against scissors, You lose")
elif user_choice == 1:
  if computer_choice == 0:
     print(f"You chose:\n {possible_choice[1]}\nComputer chose: \n{possible_choice[0]}\npaper wins against a rock, Congratulations you win!")
  else:
    print(f"You chose:\n {possible_choice[1]}\nComputer chose: \n{possible_choice[2]}\ scissor wins against paper, You lose")