
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Think you can guess my secret number between 1 and 100?")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        try:
            guess = int(input("Take a guess (1-100): "))
        except ValueError:
            print("Oops! That doesn't look like a number.")
            continue
        
        if guess < 1 or guess > 100:
            print("Please pick a number between 1 and 100.")
            continue
        
        if guess < secret_number:
            print("Too low! Aim higher.")
        elif guess > secret_number:
            print("Too high! Try a smaller number.")
        else:
            print(f"Congratulations! You guessed it ({secret_number}) in {attempts + 1} tries!")
            break
        
        attempts += 1
    
    if attempts == max_attempts:
        print(f"Sorry, you've run out of tries! The secret number was {secret_number}.")

number_guessing_game()





              



