'''
#This while loop is so you can convert multiple percentages to letter grades
while True:
    
    #Turns the input into a variable 
    grade = input(int("What is your weighted average?: "))



    if grade >= 90: 
        #This if block accounts for one letter grade for anything equal to 90 or above
        letter = "A"
    elif grade < 90 and grade >= 80:
        #These and statements go inbetween the first and second value
        letter = "B"
    elif grade < 80 and grade >= 70:
        letter = "C"
    elif grade < 70 and grade >= 60:
        letter = "D"
    elif grade < 60:
        letter = "F"


    #This prints the final message that converts the percentage to a letter grade
    print("With an average of " + str(grade) + " your letter grade is: " + letter)
'''