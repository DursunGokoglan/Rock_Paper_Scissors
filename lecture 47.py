import random

print("Welcome to Rock-Paper-Scissors!")

str_user_choice = input("Type R for Rock, P for Paper, S for Scissors: ")

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

if str_user_choice == "R":
    print(f"Your choice\n{rock}")
    user_choice = 0
elif str_user_choice == "P":
    print(f"Your choice\n{paper}")
    user_choice = 1
else:
    print(f"Your choice\n{scissors}")
    user_choice = 2

cpu_choice = random.randint(0,2)

if cpu_choice == 0 and user_choice == 0:
    print(f"Computer's choice\n{rock}")
    print("Draw!")
elif cpu_choice == 1 and user_choice == 1:
    print(f"Computer's choice\n{paper}")
    print("Draw!")
elif cpu_choice == 2 and user_choice == 2:
    print(f"Computer's choice\n{scissors}")
    print("Draw!")
elif user_choice == 0 and cpu_choice == 1:
    print(f"Computer's choice\n{paper}")
    print("Computer wins!")
elif user_choice == 0 and cpu_choice == 2:
    print(f"Computer's choice\n{scissors}")
    print("You win!")
elif user_choice == 1 and cpu_choice == 0:
    print(f"Computer's choice\n{rock}")
    print("You win!")
elif user_choice == 1 and cpu_choice == 2:
    print(f"Computer's choice\n{scissors}")
    print("Computer wins!")
elif user_choice == 2 and cpu_choice == 0:
    print(f"Computer's choice\n{rock}")
    print("Computer wins!")
elif user_choice == 2 and cpu_choice == 1:
    print(f"Computer's choice\n{paper}")
    print("You win!")