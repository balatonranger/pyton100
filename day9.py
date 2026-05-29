# A dictionary containing student names as keys and their exam scores as values
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Create an empty dictionary that will store the final grades
student_grades = {}

# Loop through each student and their score in the dictionary
for student, score in student_scores.items():

    # Check if the score is between 91 and 100 → assign "Outstanding"
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"

    # Check if the score is between 81 and 90 → assign "Exceeds Expectations"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"

    # Check if the score is between 71 and 80 → assign "Acceptable"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"

    # Any score 70 or below → assign "Fail"
    else:
        student_grades[student] = "Fail"

# Print the final dictionary showing each student and their grade
print(student_grades)
