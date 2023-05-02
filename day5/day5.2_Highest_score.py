input_list_score = input("Input list of students score: \n")

list_score = input_list_score.split(" ")

max_score = int(list_score[0])
for score in list_score:
    if max_score < int(score):
        max_score = int(score)

print(f"Max score is: {max_score}")
