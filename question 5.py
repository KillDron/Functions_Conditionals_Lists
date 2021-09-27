import random
n = 3
UW = 0
CW = 0
while n != 0:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"You chose {user_action}, computer chose {computer_action}")
    if user_action == computer_action:
        UW += 1
        CW += 1
    elif user_action == "rock":
        if computer_action == "scissors":
            UW += 1
        else:
            CW += 1
    elif user_action == "paper":
        if computer_action == "rock":
            UW += 1
        else:
            CW += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            UW += 1
        else:
            CW += 1
    n -= 1

if UW > CW:
    print("User Win")
elif UW < CW:
    print("Computer Win")
else:
    print("Draw")
