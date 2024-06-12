import random

choices = ['rock', 'paper', 'scissors']
score = 0

while True:
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        print(f"It's a tie! You and the computer both chose {player_choice}.")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        score += 1
        print(f"You win this round! You chose {player_choice} and the computer chose {computer_choice}.")
    else:
        print(f"You lose this round. You chose {player_choice} and the computer chose {computer_choice}.")

    print(f"Your current score is {score}.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print(f"Game over. Your final score is {score}.")