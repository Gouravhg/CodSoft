import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # Prompt user to choose
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue

        # Get computer's choice
        computer_choice = get_computer_choice()

        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)

        # Display the result
        display_result(user_choice, computer_choice, winner)

        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        # Display current scores
        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("\nThanks for playing!")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
