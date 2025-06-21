# student_marks.py

# Creating the dictionary with student names and marks
student_marks = {
    "Furqaan": 85,
    "Rehan": 78,
    "Talha": 92,
    "Saira": 88
}

# Asking user to input a student's name
name = "Talha"  # Simulating input

# Retrieving and displaying marks
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the record.")

# Output:
# Talha's marks: 92
