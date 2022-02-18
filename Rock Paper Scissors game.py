import random
choices = ["Rock", "Paper", "Scissors" ]
choice = random.choice(choices)
computer = choice
player = False
machine = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors? ").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            machine+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
            break
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            machine+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
            break
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            machine+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
            break
    elif player=='E':
        print("Final Scores:")
        print(f"CPU:{machine}")