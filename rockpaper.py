import random

options = ['rock', 'paper', 'scissors']

while True:
    
    user_selection= input("Enter Rock, Paper, or Scissors (or type 'quit' ): ").lower()
   
    if user_selection == 'quit':
        print("Thanks for playing! Goodbye.")
        break
    
    if user_selection not in options:
        print("Invalid input! Please choose Rock, Paper, or Scissors.")
        continue
    
    computer_choice= random.choice(options)
    print(f"Computer chose {computer_choice}.")
   
    if user_selection == computer_choice:
        print(f"Both players selected {user_selection}. It's a tie!")
    elif user_selection == 'rock':
        if computer_choice == 'scissors':
            print("You win!")
        else:
            print(" You lose.")
    elif user_selection == 'paper':
        if computer_choice == 'rock':
            print("You win!")
        else:
            print(" You lose.")
    elif user_selection == 'scissors':
        if computer_choice == 'paper':
            print("You win!")
        else:
            print("You lose.")
