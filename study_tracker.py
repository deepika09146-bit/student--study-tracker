def add_study_hours():
    subject = input("Enter subject name: ")
    hours = float(input("Enter number of hours studied: "))

    with open("study_log.txt", "a") as file:
        file.write(f"{subject} - {hours} hours\n")

    print("Study hours added successfully!")

def view_study_log():
    try:
        with open("study_log.txt", "r") as file:
            print("\nStudy Log:")
            print(file.read())
    except FileNotFoundError:
        print("No study log found yet.")

while True:
    print("\n1. Add Study Hours")
    print("2. View Study Log")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_study_hours()
    elif choice == "2":
        view_study_log()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
