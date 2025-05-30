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
user_choice = input("Type 0 for Rock, 1 for Paper and 2 for Scissors ")
if user_choice == "0":
    print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)
else:
    print("Please enter either 0 or 1 or 2")

if user_choice == "0" or user_choice == "1" or user_choice == "2":
    computer_choice = random.choice(["0", "1", "2"])
    if computer_choice == "0":
        print(f"The computer chooses: \n {rock}")
    elif computer_choice == "1":
        print(f"The computer chooses: \n {paper}")
    else:
        print(f"The computer chooses: \n {scissors}")

    if (user_choice == "0" and computer_choice == "2") or (user_choice == "1" and computer_choice == "0") or (
            user_choice == "2" and computer_choice == "1"):
        print("Yay! YOU WIN!")
    elif user_choice == computer_choice:
        print("It's a draw. Try again")
    else:
        print("Better luck next time.")