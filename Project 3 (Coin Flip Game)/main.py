
import random

def coin_toss():
    options = ["Heads", "Tails"]
    user_choice = input("Choose Heads or Tails: ").capitalize() # getting input by user

    if user_choice not in options:
        print("Invalid choice! Please choose Heads or Tails.")
        return

    computer_choice = random.choice(options)
    print(f"The coin landed on: {computer_choice}")

    if user_choice == computer_choice:
        print("Congratulations! You won! 🎉")
    else:
        print("Oops! You lost. Try again!")

# Run the game
coin_toss()
