# Week 1 Challenge: Number Guessing Game

import random  # This gives our robot a pair of dice!

def guessing_game():
    print("\n-----------------------------------------------")
    print("      Welcome to the Number Guessing Game!")
    print("-----------------------------------------------")
    
    # 1. The robot picks a secret number between 1 and 10
    secret_number = random.randint(1, 50)
    
    print("I am thinking of a number between 1 and 50...")

    # 2. Start the guessing loop!
    while True:
        # Ask the player for their guess and turn it into a math number
        guess = int(input("What is your guess? "))

        # 3. The Sorting Hat (Checking the guess)
        if guess < secret_number:
            print("Too low! 📉 Try again.")
        elif guess > secret_number:
            print("Too high! 📈 Try again.")
        else:
            print("🎉 YOU GOT IT! The secret number was", secret_number)
            break  # This stops the game!

# Pressing the start button!
guessing_game()