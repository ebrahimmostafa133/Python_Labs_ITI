def createStudentsFile(path="students.txt"):
    students_data = [
        "1,Benzema",
        "2,Ebrahim Benzema",
        "3,Benzema Ebrahim",
    ]
    with open(path, "w") as f:
        for line in students_data:
            f.write(line + "\n")

# ===================================================
def createGradesFile(path="grades.txt"):
    grades_data = [
        "1,Python,85",
        "1,Math,90",
        "1,English,88",
        "2,Python,78",
        "2,Math,88",
        "2,English,75",
        "3,Python,92",
        "3,Math,75",
        "3,English,85",
    ]
    with open(path, "w") as f:
        for line in grades_data:
            f.write(line + "\n")

# ===================================================
def addGrade(path="grades.txt"):
    with open(path, "a") as f:
        student_id = input("Enter student ID: ").strip()
        subject = input("Enter subject: ").strip()
        grade = input("Enter grade: ").strip()
        f.write(f"{student_id},{subject},{grade}\n")
    print("Grade added successfully.")

# ===================================================
def addStudent(path="students.txt"):
    with open(path, "a") as f:
        student_id = input("Enter student ID: ").strip()
        student_name = input("Enter student name: ").strip()
        f.write(f"{student_id},{student_name}\n")
    print("Student added successfully.")
