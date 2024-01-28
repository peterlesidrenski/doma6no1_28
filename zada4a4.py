def calculate_average(grades):
    return sum(grades) / len(grades)
num_students = int(input("Въведете брой съученици: "))
students_data = {}
for _ in range(num_students):
    student_name = input("Въведете име на съученик: ")
    student_grades = [float(input(f"Въведете оценка за {student_name}: ")) for _ in range(num_students)]
    students_data[student_name] = student_grades
for student_name, grades in students_data.items():
    average_grade = calculate_average(grades)
    print(f"{student_name}: {average_grade:.2f}")
