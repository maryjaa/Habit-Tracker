import datetime
from datetime import date

# an empty list of habits and a dictionary to store the habit tracking data
habits = []
tracker = {}

# a function to load the habit names and tracking data from a text file
def load_data():
    with open("habits.txt", "r") as f:
        data = f.readlines()
        for line in data:
            habit, dates = line.strip().split(":")
            habits.append(habit)
            tracker[habit] = [date for date in dates.split(" ")]

# a function to save the habit names and tracking data to a text file
def save_data():
    with open("habits.txt", "w") as f:
        for habit in habits:
            dates = " ".join(tracker[habit])
            f.write(f"{habit}:{dates}\n")

# a function to add a new habit
def add_habit(habit_name):
    habits.append(habit_name)
    tracker[habit_name] = []
    save_data()

# a function to delete a habit
def delete_habit(habit_name):  #todo: error handling when user enters a habit name that doesn't exist
    habits.remove(habit_name)
    del tracker[habit_name]
    save_data()

# a function to mark the habit (add a date to a habit's tracking data)
def mark_habit(habit_name):
    today = date.today().strftime("%Y-%m-%d")
    tracker[habit_name].append(today)
    save_data()

# a function to calculate the current streak for a habit
def current_streak(habit_name):
    dates = tracker[habit_name]
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    streak = 0
    max_streak = 0
    for i in range(len(dates) -1, -1, -1):
        date1 = datetime.datetime.strptime(dates[i], "%Y-%m-%d")
        if i > 0:
            date2 = datetime.datetime.strptime(dates[i-1], "%Y-%m-%d")
            delta = (date1 - date2).days
            if delta == 1:
                streak += 1
                if streak > max_streak:
                    max_streak = streak
            else:
                streak = 0
        if dates[i] == today:
            break
    return max_streak

# a function to display the calendar of a habit
def display_calendar(habit_name, year, month):
    dates = tracker[habit_name]
    print(f"{habit_name} ({month} {year})")
    print("-" * (len(habit_name) + 14))
    print("| Su Mo Tu We Th Fr Sa |")
    print("| -- -- -- -- -- -- -- |")
    calendar = [[] for i in range(7)]
    for date in dates:
        week_day = (datetime.datetime.strptime(date, "%Y-%m-%d").weekday() + 1) % 7
        calendar[week_day].append(date[-2:])
    for row in calendar:
        line = " ".join(row)
        line = line.ljust(20, " ")
        print(f"| {line} |")
    print("| -- -- -- -- -- -- -- |")
    print("\n")

#! MAIN MENU

def main_menu():
    load_data()
    while True:
        print("Habit Tracker")
        print("=" * len("Habit Tracker"))
        print("1. See all existing habits")
        print("2. Display the calendar")
        print("3. Add a new habit")
        print("4. Delete a habit")
        print("5. See current streaks for every habit")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            for habit in habits:
                print(habit)
        elif choice == "2":
            habit = input("Enter the name of the habit to display: ")
            year = int(input("Enter the year: "))
            month = int(input("Enter the month (f.ex. for January, enter 01): "))
            display_calendar(habit, year, month)
        elif choice == "3":
            habit_name = input("Enter the name of the new habit: ")
            add_habit(habit_name)
        elif choice == "4":
            habit_name = input("Enter the name of the habit to delete: ")
            delete_habit(habit_name)
        elif choice == "5":
            for habit in habits:
                print(f"{habit}: {current_streak(habit)}")
        elif choice == "6":
            save_data()
            break
        else:
            print("Invalid choice. Try again.")

main_menu()






