import random as rd

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_print = [rock, paper, scissors]

game = ["rock", "paper", "scissors"]

computer_choice = rd.randint(0, 2)

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice == 0 and computer_choice == 1:
    print(
        f"computer choose: {game[computer_choice]}\n {list_print[computer_choice]} \n you choose: {game[player_choice]}"
        f" \n {list_print[player_choice]} \n You Lose")
elif player_choice == 0 and computer_choice == 2:
    print(
        f"computer choose: {game[computer_choice]}\n {list_print[computer_choice]} \n you choose: {game[player_choice]}"
        f" \n {list_print[player_choice]} \n You Win")
elif player_choice == 1 and computer_choice == 0:
    print(
        f"computer choose: {game[computer_choice]}\n {list_print[computer_choice]} \n you choose: {game[player_choice]}"
        f" \n {list_print[player_choice]} \n You Win")
elif player_choice == 1 and computer_choice == 2:
    print(
        f"computer choose: {game[computer_choice]}\n {list_print[computer_choice]} \n you choose: {game[player_choice]}"
        f" \n {list_print[player_choice]} \n You Lose")
elif player_choice == 2 and computer_choice == 0:
    print(
        f"computer choose: {game[computer_choice]}\n {list_print[computer_choice]} \n you choose: {game[player_choice]}"
        f" \n {list_print[player_choice]} \n You Lose")
elif player_choice == 2 and computer_choice == 1:
    print(
        f"computer choose: {game[computer_choice]}\n {list_print[computer_choice]} \n you choose: {game[player_choice]}"
        f" \n {list_print[player_choice]} \n You Win")
else:
    print(
        f"computer choose: {game[computer_choice]}\n {list_print[computer_choice]} \n you choose: {game[player_choice]}"
        f"\n {list_print[player_choice]} \n DRAW")
