print("Student Rank Processing Engine")

number = int(input("Enter number of students: "))

student= []

for i in range(number):

    print("\nEnter details of student", i + 1)

    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")

    mark1 = float(input("Enter marks of Python: "))
    mark2 = float(input("Enter marks of MEARN Stack: "))
    mark3 = float(input("Enter marks of Cyber Security: "))
    mark4 = float(input("Enter marks of Data Analitics: "))
    mark5 = float(input("Enter marks of Matchine Learning :"))

    total = mark1 + mark2 + mark3 + mark4 + mark5
    percentage = total / 5

    # Grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Dictionary
    Student = {
        "roll": roll,
        "name": name,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    student.append(Student)


# Sorting by percentage  highest first
for i in range(number):
    for j in range(i + 1, number):
        if student[i]["percentage"] < student[j]["percentage"]:
            temp = student[i]
            student[i] = student[j]
            student[j] = temp


print("\n STUDENT RANKING LIST ")

rank = 1

for i in range(number):

    if i == 0:
        rank = 1
    elif student[i]["percentage"] != student[i - 1]["percentage"]:
        rank = i + 1

    print("\nRank:", rank)
    print("Roll No:", student[i]["roll"])
    print("Name:", student[i]["name"])
    print("Total:", student[i]["total"])
    print("Percentage:", student[i]["percentage"])
    print("Grade:", student[i]["grade"])
