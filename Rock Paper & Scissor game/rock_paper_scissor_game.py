import random

user_input = input("Enter your move = rock, paper, scissor: ")
item_list = ["rock", "paper", "scissor"]
computer_input = random.choice(item_list)
print(f"user choice = {user_input}, computer choice = {computer_input}")

if user_input == computer_input:
    print("both chooses same: = Match Tie")
elif user_input == "rock":
    if computer_input == "paper":
        print("computer win")
    else:
        print("user win")
elif user_input == "paper":
    if computer_input == "rock":
        print("user win")
    else:
        print("computer win")
elif user_input == "scissor":
    if computer_input == "paper":
        print("user win")
    else:
        print("computer win")
