# importation
import random
import string
import time

# welcome messages
print("Welcome!")
time.sleep(0.5)
print("I see you'd like to generate a strong password")
time.sleep(1.0)

# Input of length
password_question = (int(input("\nSelect the length for your password > ")))
time.sleep(1.0)

# Data format
lower_cases = string.ascii_lowercase
upper_cases = string.ascii_uppercase
number_cases = string.digits

# combined data to create pass
combined = (lower_cases + upper_cases + number_cases)
uppercase = (upper_cases)
lowercase = (lower_cases)

password_generated = "".join(random.sample(combined,password_question))
print(f"Here is your password: {password_generated}")


