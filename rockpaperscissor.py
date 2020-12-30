import random
# declaring global variables

game_still_going = True

# Declaring the default user and computer value to None
user_choice = None
computer_choice = None

# Declaring the default user and human score to 0
user_score = 0
computer_score = 0

# Creating dictionary for game items
game_dict = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors',
}


# function to play the game
def play_game():
    print("Go through some instructions.")
    print("""
        r - rock
        p - paper
        s - scissors
        q - quit
        Let's Start the game
    """)

    while game_still_going:
        ask_user_input()

        get_computer_input()

        compare_both_inputs()

        display_score()


# function to ask input from the user
def ask_user_input():
    global user_choice

    user_choice = input("Choose your choice(Rock(r) / Paper(p) / Scissors(s)): ").lower()
    while user_choice not in ['r', 'p', 's', 'q']:
        print("You have entered incorrect input")
        print("R -> Rock, P -> Paper, S -> Scissors")
        user_choice = input("Choose your choice(Rock(r) / Paper(p) / Scissors(s)): ").lower()

    if user_choice == 'q':
        quit_game()
    else:
        user_choice = game_dict.get(user_choice)
        print(f'Your choice: {user_choice}')
    return user_choice


def get_computer_input():
    global computer_choice

    computer_choice = random.choice(list(game_dict.values()))
    print(f'Computer choice: {computer_choice}')
    return computer_choice


def compare_both_inputs():
    global user_choice, computer_choice, user_score, computer_score

    if user_choice == 'Rock' and computer_choice == 'Paper':
        print("Computer won")
        computer_score += 1
    elif user_choice == 'Rock' and computer_choice == 'Scissors':
        print("You won")
        user_score += 1
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        print("You won")
        user_score += 1
    elif user_choice == 'Paper' and computer_choice == 'Scissors':
        print("Computer won")
        computer_score += 1
    elif user_choice == 'Scissors' and computer_choice == 'Rock':
        print("Computer won")
        computer_score += 1
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        print("User won")
        user_score += 1
    else:
        print("Nobody won")
    return user_score, computer_score


def display_score():
    global user_score, computer_score
    print(f'Your Score: {user_score}')
    print(f'Computer Score: {computer_score}')


def quit_game():
    global game_still_going, user_score, computer_score
    game_still_going = False
    if user_score > computer_score:
        print("Overall winner: You")
    elif computer_score > user_score:
        print("Overall winner: Computer")
    else:
        print("Match draw")
    exit()


play_game()


# Python program for playing Rock Paper Scissor
#
# 1. Start the game
# 2. Ask input from the user
# 3. Make computer to choose one input
# 4. Compare the input
# 5. Announce the winner
