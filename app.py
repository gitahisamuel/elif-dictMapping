score=int(input("Enter your score: " ))

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





def get_grades (score):
    if score >= 70:
        return "A"
    elif 60 <= score < 70:
        return "B"
    elif 50 <= score < 60:
        return "C"
    elif 40 <= score < 50:
        return "D"
    else:
        return "E"

def generate_message(grades):
    grade_message = {
        "A": "You have scored an A - Exceptional!",
        "B": "You have scored a B - Excellent!",
        "C": "You have scored a C - Good!",
        "D": "You have scored a D - Do better!",
        "E": "You have scored a E - You have failed!",
    }
    return grade_message[grades]

# print(get_grades(30))
score =int(input("Input your score: "))
grades = get_grades(score)
print(generate_message(grades))
