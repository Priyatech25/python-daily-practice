try:
    f = open("test.txt")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution finished")
