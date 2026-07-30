python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

student_score = list(set([student[1] for student in python_students]))

student_score.sort()

target_score = student_score[1]

print(target_score)

student_name = [student[0] for student in python_students if student[1] == target_score]

student_name.sort()

for name in student_name:
	print(name)