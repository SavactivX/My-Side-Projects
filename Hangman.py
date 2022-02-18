import time
import random

pc_games = ['forzahorizon', 'rocketleague', 'counterstrikeglobaloffensive', 'callofduty', 'valorant']
word = random.choice(pc_games)
guesses = ''
turns = 5
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
time.sleep(1)
print("Start guessing...\n")
time.sleep(0.5)

# A List Of Secret Words

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end=""),
            failed += 1
    if failed == 0:
        print("\nYou won")
        break
    guess = input("\n\nguess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("\nWrong")
        print("\nYou have", + turns, 'more guesses')
        if turns == 0:
            print(f"\nYou Lose. The correct answer is {word}")
