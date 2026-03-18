from School.fileCreator import createStudentsFile, createGradesFile
from School.student_grade import findStudent
# ========================================
#   Task 1: Create students.txt & grades.txt
# ========================================
createStudentsFile()
createGradesFile()

# ========================================
#   Task 2: Read & Display All Student Names
# ========================================
def displayStudents(path="students.txt"):
    print("All Students:")
    print("="*30)
    with open(path,"r")as f:
        for line in f:
            line = line.strip()
            if line:
                id,name=line.split(",", 1)
                print(f"  ID: {id} | Name:{name}")
    print("="*30)

displayStudents()
# ========================================
#   Task 3: Display Grades for a Subject
# ========================================
def displaySubjectGrades(path="grades.txt", subject="Python"):
    print(f"{subject} Grades:")
    print("="*30)
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                id, subj, grade = line.split(",", 2)
                if subj == subject:
                    print(f"  ID: {id} | Subject: {subj} | Grade: {grade}")
    print("="*30)

displaySubjectGrades()
# ========================================
#   Task 4: Lookup Student by ID
# ========================================
findStudent(student_id="1")

# ========================================
#   Task 5: Calculate Average Grade per Student
# ========================================
def displayAverages(students_path="students.txt", grades_path="grades.txt"):

    students = {}
    with open(students_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                sid, name = line.split(",", 1)
                students[sid] = name

    grades = {}
    with open(grades_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                sid, subject, grade = line.split(",")
                grades.setdefault(sid, []).append(int(grade))

    print("Average Students Grades:")
    print("="*30)
    for sid,name in students.items():
        if sid in grades:
            avg = sum(grades[sid]) /len(grades[sid])
            print(f"ID: {sid} | Student Name: {name} | Average Grade: {avg:.2f}")
    print("="*30)
displayAverages()
