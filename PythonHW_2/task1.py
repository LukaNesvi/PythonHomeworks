student_name = "luka"
math_grade = 5
physics_grade = 4
english_grade = 5
gpa = (math_grade + physics_grade + english_grade) / 3

print (f"Hello {student_name}, your grades are: \nMath: {math_grade}\nPhysics: {physics_grade}\nEnglish: {english_grade}")
print (f"And your total GPA is: {round(gpa, 1)}")