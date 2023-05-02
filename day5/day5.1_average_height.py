ip = input("Input list of student height: \n")
student_heights = ip.split(" ")

total_height = 0
for height in student_heights:
    total_height += int(height)

print(f"average: {total_height / len(student_heights)}")
