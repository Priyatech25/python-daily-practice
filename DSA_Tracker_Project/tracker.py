# MINI PROJECT - DSA TRACKER

problems = []

def add_problem():
    day = input("Enter day number: ")
    topic = input("Enter topic (Array/Tree/Graph/etc): ")
    name = input("Enter problem name: ")

    problem = {
        "day": day,
        "topic": topic,
        "name": name,
        "status": "Not Done"
    }

    problems.append(problem)
    print("Problem added!\n")


def view_problems():
    if not problems:
        print("No problems added.\n")
        return

    for i, p in enumerate(problems):
        print(f"{i+1}. Day {p['day']} | {p['topic']} | {p['name']} | {p['status']}")
    print()


def mark_done():
    view_problems()
    try:
        index = int(input("Enter problem number to mark done: ")) - 1
        problems[index]["status"] = "Done"
        print("Marked as completed!\n")
    except:
        print("Invalid choice!\n")


def show_progress():
    total = len(problems)
    done = sum(1 for p in problems if p["status"] == "Done")

    if total == 0:
        print("No progress yet.\n")
        return

    percent = (done / total) * 100
    print(f" Progress: {done}/{total} completed ({percent:.2f}%)\n")


def menu():
    while True:
        print("1. Add Problem")
        print("2. View Problems")
        print("3. Mark as Done")
        print("4. Show Progress")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_problem()
        elif choice == "2":
            view_problems()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            show_progress()
        elif choice == "5":
            print("Goodbye ")
            break
        else:
            print("Invalid choice!\n")


# Run program
menu()