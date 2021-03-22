
def get_winner(player_action, computer_action):
    win = False

    if player_action == computer_action:
        print(f"Both players selected {player_action}. It's a tie!")
        win = 'tie'
    elif player_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            win = True
        else:
            print("Paper covers rock! You lose.")
    elif player_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            win = True
        else:
            print("Scissors cuts paper! You lose.")
    elif player_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            win = True
        else:
            print("Rock smashes scissors! You lose.")

    return win