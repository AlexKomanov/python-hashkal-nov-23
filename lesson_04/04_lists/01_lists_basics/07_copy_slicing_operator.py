students_grades = [75, 80, 90, 85, 65, 30]

updated_grades = students_grades[:]

print(students_grades)
print(updated_grades)

students_grades[0] = 0
students_grades[-1] = 0

print(students_grades)
print(updated_grades)

print(id(students_grades))
print(id(updated_grades))
