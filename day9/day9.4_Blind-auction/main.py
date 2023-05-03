from art import logo
import os

print(logo)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


bids = {}


def find_highest_bidder(budding_record):
    highest_bid = 0
    winner = ""
    for bidder in budding_record:
        bid_amount = budding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


is_end = False
while not is_end:
    name = input("What is your name? ")
    price = float(input("What is your bid? "))

    bids[name] = price
    continue_bids = input("Are there any other bidders? Type 'y' or 'n'.\n")
    if continue_bids == 'y':
        print(f"****")
    else:
        print('No')
        is_end = True
        find_highest_bidder(bids)
