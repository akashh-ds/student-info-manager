students = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    students.append({"name": name, "roll": roll, "marks": marks})
    print("✅ Student added successfully!\n")

def view_students():
    for s in students:
        print(f"{s['roll']} | {s['name']} | Marks: {s['marks']}")

while True:
    print("\n1. Add Student\n2. View All\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid option.")