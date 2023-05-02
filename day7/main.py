import hangman_art as ha
import hangman_words as hw
import random

print(ha.logo)
random_words = random.choice(hw.word_list)
print(f'Pssst, the solution is {random_words}.')

blank_words = []
for i in random_words:
    blank_words.append("_")

continue_of_game = True
state = len(ha.stages) - 1
numbers_of_banks = len(blank_words)
print(f"Word is: {blank_words}")
while continue_of_game:
    if state == 0:
        print("You lose")
        continue_of_game = False
    char = input("Guess a letter: \n")
    temp = numbers_of_banks
    for x in range(len(random_words)):
        if char == random_words[x]:
            blank_words[x] = char
            numbers_of_banks -= 1
    if temp <= numbers_of_banks:
        print(f"You lose a life \n {ha.stages[state]}")
        state -= 1
    print(f"{blank_words}")

    if "_" not in blank_words:
        print("You Win")
        continue_of_game = False
