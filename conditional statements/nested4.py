# Prompt the user to enter the number of students
n = int(input("Enter the number of students: "))

# Create an empty list to store the student names and grades
students = []

# Loop to input the names and grades of each student
for _ in range(n):
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students.append([name, grade])

# Find the second lowest grade
lowest_grade = float('inf')
second_lowest_grade = float('inf')

for _, grade in students:
    if grade < lowest_grade:
        second_lowest_grade = lowest_grade
        lowest_grade = grade
    elif grade < second_lowest_grade and grade != lowest_grade:
        second_lowest_grade = grade

# Find the students with the second lowest grade
second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]

# Sort the names alphabetically
second_lowest_students.sort()

# Print the names of the students with the second lowest grade
print("Student(s) with the second lowest grade:")
for name in second_lowest_students:
    print(name)