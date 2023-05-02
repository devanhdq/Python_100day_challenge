row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map_ = [row1, row2, row3]

index_ = input("Enter index:\n")

row = int(index_[0])
column = int(index_[1])

map_[column - 1][row - 1] = " X "

print(f"{map_[0]}\n{map_[1]}\n{map_[2]}")
