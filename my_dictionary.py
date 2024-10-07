
student_grades = {"Alice": 90, "Bob": 85, "Charlie": 92}


print(student_grades)
#student_1 = student_grades["Alice"]
#print("sudent:", student_1)

# current_grade = input("Enter the name of the student you are searching for: ")
# print(f"The grade for {current_grade} is: {student_grades[current_grade]}")

student_grades["David"] = 88
student_grades["Bob"] = 87
print("This is the updated Dictionary: ", student_grades)

# del student_grades["Charlie"]
# student_grades.pop("Bob")
# print(student_grades)

# if "Alice" in student_grades:
#     print("Alice's grade is", student_grades["Alice"])

for name, grade in student_grades.items():
    print(name, "has a grade of", grade)