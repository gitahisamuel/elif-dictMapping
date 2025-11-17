#pseudocode
#A list of name and scores is already given (array of object)
#our program should print 
# 1- each student in our dict the score and the message
 #we loop through our dict for stud in students we print but here we use if construct
  # and maybe a dict for comments if (score ,<=>=...grade...)
# 2- grade summary where our programs counts and displays how many students fall in each grade 
# category
#our code will have two parts


students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 48},
    {"name": "Chris", "score": 72},
    {"name": "Diana", "score": 90},
    {"name": "Elvis", "score": 60}
]

for student in students:
     name = student["name"]
     score = student["score"]

if score >=80 and score <= 100:

    grade = 'A'
elif score >=70 and score < 80:
   
    grade = 'B'
elif score >=60 and score < 70:
   
    grade = 'C'
elif score >=50 and score <60:
 
    grade = 'D'
else:

    grade = 'E'

comments = { 
    'A' : "Excelent work",
    'B' : "Good work",
    'C' : "Average work",
    'D' : "Do better work",
    'E' : " work",
}   

print(f"Your grade is {grade}")
print(comments[grade])
    





"""Given a list of students’ scores, write a Python program that:

1. Prints each student’s name, score, and grade message.
2. Counts and displays how many students fall in each grade category.

input example:

[
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 48},
    {"name": "Chris", "score": 72},
    {"name": "Diana", "score": 90},
    {"name": "Elvis", "score": 60}
]
Output example:

Alice scored 85 → Very Good
Bob scored 48 → Fail
Chris scored 72 → Good
Diana scored 90 → Excellent
Elvis scored 60 → Pass


Grade Summary:
Fail: 1 student(s)
Pass: 1 student(s)
Good: 1 student(s)
Very Good: 1 student(s)
Excellent: 1 student(s)
"""

# STEP 1: Determine grade/comment category based on score
# Write a function that takes a score and returns the appropriate grade/comment

# STEP 2: Initialize a dictionary to count students in each grade category
# To track how many students fall into each category

# STEP 3: Loop through each student, determine their grade, and print the result
# Also increment the count for their grade category

# STEP 4: Print the summary showing how many students are in each category

# STEP 5: Input data

# STEP 6: Execute the program


#STEP 1
def get_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Very Good"
    elif score >= 60:
        return "Good"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"

#STEP 2
def print_student_grades(students):
    # Initialize how many students per category
    grade_counts = {
        "Fail": 0,
        "Pass": 0,
        "Good": 0,
        "Very Good": 0,
        "Excellent": 0
    }
    
    #STEP 3
    # Process each student
    for student in students:
        name = student["name"]
        score = student["score"]
        grade = get_grade(score)
        
        print(f"{name} scored {score} → {grade}")
        
        # Update counter
        grade_counts[grade] += 1
    
    return grade_counts

#STEP 4
def print_grade_summary(grade_counts):
    print("\n\nGrade Summary:")
    
    # Define order
    grade_order = ["Fail", "Pass", "Good", "Very Good", "Excellent"]
    
    for grade in grade_order:
        count = grade_counts[grade]
        print(f"{grade}: {count} student(s)")

# STEP 5
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 48},
    {"name": "Chris", "score": 72},
    {"name": "Diana", "score": 90},
    {"name": "Elvis", "score": 60}
]

# STEP 6
grade_counts = print_student_grades(students)
print_grade_summary(grade_counts)
