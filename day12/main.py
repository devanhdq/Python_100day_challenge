from art import logo
import random

print(logo)

computer_random = random.randint(1, 100)


# computer_random = 10


def compare_number(player_number, computer_number):
    if player_number > computer_number:
        return 1
    elif player_number < computer_number:
        return -1
    else:
        return 0


def compare_input():
    player_number = int(input('Make a guess: '))
    compare = compare_number(player_number, computer_random)
    return compare


def check_end_game(times):
    end_game = False
    while not end_game:
        state_game = compare_input()
        if times == 0:
            end_game = True
            print("You Lose")
        elif state_game == 0:
            end_game = True
            print("You Win")
        elif state_game == 1:
            print("Lower")
            print(f"You have {times} attempts remaining to guess the number.")
        elif state_game == -1:
            print("Higher")
            print(f"You have {times} attempts remaining to guess the number.")
        times -= 1


print('''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
''')

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == 'easy':
    print('You have 10 attempts remaining to guess the number.')
    check_end_game(10)
else:
    print('You have 5 attempts remaining to guess the number.')
    check_end_game(5)
