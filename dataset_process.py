import os

photos = os.listdir("./data/image/train/")

with open("./data/dataset.txt", "w") as f:
    for photo in photos:
        name = photo.split(".")[0]
        if name == "cat":
            f.write(photo+";0\n")
        else:
            f.write(photo + ";1\n")
f.close()