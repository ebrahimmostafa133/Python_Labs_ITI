def findStudent(students_path="students.txt", grades_path="grades.txt", student_id="1"):
    student_name = ""
    with open(students_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                sid, name = line.split(",", 1)
                if sid == student_id:
                    student_name = name
                    print(f"Student: {student_name} (ID: {student_id})")
                    findStudentGrades(student_id=student_id)
                    break
    if not student_name:
        print(f"No student found with ID '{student_id}'.")
    


def findStudentGrades(students_path="students.txt", grades_path="grades.txt", student_id="1"):
    found_grades = False
    with open(grades_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                sid, subject, grade = line.split(",", 2)
                if sid == student_id:
                    print(f"  {subject}: {grade}")
                    found_grades = True
    if not found_grades:
        print(f"No grades found for student ID '{student_id}'.")
    
    
