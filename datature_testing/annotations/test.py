with open("train.txt", "r") as trainfile:
    file_lines = [f"../assets/{x}" for x in trainfile.readlines()]

with open("train2.txt", 'w') as f:
    f.writelines(file_lines)