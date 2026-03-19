#                                         # Student_Grade_Manager

# students = {}

# while True:
#     name = input("Enter student name (or 'done' to finish): ")
#     if name.lower() == 'done':
#         break

#     try:
#         marks = float(input(f"Enter marks for {name}: "))
#         if marks < 0 or marks > 100:
#             print("Marks must be between 0 and 100.")
#             continue
#         students[name] = marks
#     except ValueError:
#         print("Please enter a valid number.")

# if not students:
#     print("No student data entered.")
# else:
#     print("\n--- Student Grades ---")

#     total = sum(students.values())
#     average = total / len(students)
#     highest = max(students.values())
#     lowest = min(students.values())

#     for name, marks in students.items():
#         if marks >= 90:
#             grade = "A"
#         elif marks >= 75:
#             grade = "B"
#         elif marks >= 60:
#             grade = "C"
#         else:
#             grade = "Fail"

#         print(f"{name}: Marks = {marks}, Grade = {grade}")

#     print("\n--- Statistics ---")
#     print(f"Average Marks: {average:.2f}")
#     print(f"Highest Marks: {highest}")
#     print(f"Lowest Marks: {lowest}")

students = {}

while True:
    first_name = input("Enter student first name (or 'done' to finish): ")
    if first_name.lower() == 'done':
        break

    last_name = input("Enter student last name: ")
    full_name = f"{first_name} {last_name}"

    try:
        marks = float(input(f"Enter marks for {full_name}: "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            continue

        students[full_name] = marks

    except ValueError:
        print("Please enter a valid number.")

if not students:
    print("No student data entered.")
else:
    print("\n--- Student Grades ---")

    total = sum(students.values())
    average = total / len(students)
    highest = max(students.values())
    lowest = min(students.values())

    for name, marks in students.items():
        if marks >= 90:
            grade = "A"
            message = "Excellent work! 🎉 Congratulations!"
        elif marks >= 75:
            grade = "B"
            message = "Great job! Keep it up 👏"
        elif marks >= 60:
            grade = "C"
            message = "Good effort, you can do even better 🙂"
        else:
            grade = "Fail"
            message = "Don't give up — keep practicing 💪"

        print(f"{name}: Marks = {marks}, Grade = {grade}")
        print(f"➡ {message}\n")

    print("--- Statistics ---")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
