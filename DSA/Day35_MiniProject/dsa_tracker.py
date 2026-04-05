# DAY 35 - Mini Project: DSA Practice Tracker

import json
import os

FILE = "dsa_progress.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_problem(data):
    day = input("Enter day number: ")
    topic = input("Enter topic (Array/Linked List/Tree/etc): ")
    problem = input("Enter problem name: ")

    if day not in data:
        data[day] = []
    data[day].append({"topic": topic, "problem": problem})
    save_data(data)
    print("Problem added successfully!\n")

def view_progress(data):
    if not data:
        print("No progress yet!")
        return
    for day, problems in sorted(data.items()):
        print(f"\nDay {day}:")
        for p in problems:
            print(f" - {p['topic']}: {p['problem']}")

def main():
    data = load_data()
    while True:
        print("\n--- DSA Tracker ---")
        print("1. Add Problem")
        print("2. View Progress")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_problem(data)
        elif choice == "2":
            view_progress(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()