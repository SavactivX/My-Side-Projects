name = input("What is your name? ")
if len(name) < 3:
    print("Name must be 3 characters long")
elif len(name) > 50:
    print("Name must be a maximum or 50 characters long")
else: print("Hi " + name )
color = input("what is your favorite color? ")
print("Perfect color")
Age = input("What is your age? ")
if Age == 18 :
    print("Score those A+ in university")
else:
    print("Score those A+ in school")
weight = int(input('What is your weight? '))
unit = input('(L)bs or (K)g: ')
if unit.upper() ==  "L":
    converted = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')
Class = input("What grade are you in? ")
if Class == 13:
    print("Woah!, you must be lucky to finish school ")
else:
    print("Have patience. You will complete school soon")
Information = print(f"Based on your information, I see your name is {name} and your weight is {weight}" )
BMI = print("Let's calculate your BMI")
height = float(input("Enter your height in cm: "))
BMI = weight / (height/100)**2.
print(f"You BMI is {BMI}")
import random
question = input("Would you like to Play a short guessing game? ")
if question == ("Yes" or "yes"):
    print("Guess a number between 1-10")
    for i in range(1):
        secrets =  (random.randint(1,10))
    secret_number = secrets
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input('Guess: '))
        guess_count += 1
        if guess == secret_number:
            print("You Won")
            break
    else:
        print(f"Sorry you failed. Correct answer is {secrets}")
else:
    print("Aight ")
Good_day = input("Would you like to thank the creator of this questionaire? ")
if Good_day == ("Yes").capitalize():
    print("Thanks for your answer and time in doing this questionaire" )
else:
    print("I am sorry for any inconveniece. Thank you for your time in doing this questionaire")



