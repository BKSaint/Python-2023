

while True:
    
    grade = int(input("What is your weighted average?: "))

    if grade >= 90:
        letter = "A"
    elif grade < 90 and grade >= 80:
        letter = "B"
    elif grade < 80 and grade >= 70:
        letter = "C"
    elif grade < 70 and grade >= 60:
        letter = "D"
    elif grade < 60:
        letter = "F"

    print("With an average of " + str(grade) + " your letter grade is: " + letter)
