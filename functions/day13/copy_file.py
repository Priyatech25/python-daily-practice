# copy_file.py
with open("data.txt") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())
