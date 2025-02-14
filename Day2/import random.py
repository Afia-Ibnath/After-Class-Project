import random
choices = ["rock", "paper", "scissors"]
def determine_winner(player, ai):
    if player == ai:
        return "It's a tie!"
    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        return "You win!"
    else:
        return "AI wins!"
while True:
    print("\nRock, Paper, Scissors - Let's Play!")
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    
    if player_choice == "quit":
        print("Thanks for playing! Goodbye!")
        break
    elif player_choice not in choices:
        print("Invalid choice, try again.")
        continue
    
    ai_choice = random.choice(choices)
    
    print(f"AI chose: {ai_choice}")
    print(determine_winner(player_choice, ai_choice))
