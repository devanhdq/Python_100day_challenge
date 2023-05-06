from art import logo, vs
from data import data
import random

length_data = len(data)


def random_data(this):
    result = data[random.randint(0, length_data)]
    if this is None:
        return result
    while data.index(this) == data.index(result):
        result = data[random.randint(0, length_data)]
    return result


obj1 = random_data(None)
score = 0


def compare_object(data1, data2):
    if data1['follower_count'] > data2['follower_count']:
        return 1
    elif data1['follower_count'] < data2['follower_count']:
        return -1
    else:
        return 0


def check_answer(result_compare, answer):
    if (answer == 'A' and result_compare == 1) or (answer == "B" and result_compare == -1):
        return True
    else:
        return False


print(logo)


def run_game(object1):
    obj2 = random_data(object1)
    compare_obj1_and_obj2 = compare_object(object1, obj2)
    print(f"Compare A: {object1['name']},{object1['follower_count']} {object1['description']}, {object1['country']} ")
    print(vs)
    print(f"Compare B: {obj2['name']}, {obj2['follower_count']} {obj2['description']}, {obj2['country']} ")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if check_answer(compare_obj1_and_obj2, answer):
        global score
        score += 1
        run_game(obj2)
    else:
        print(f"You Lose!! You have {score} score")


run_game(obj1)
