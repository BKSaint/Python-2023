grade = []
sum = 0
counter = 1
items = int(input("How many classes/assignments do you want to average?: "))


while items > 0:
    grade.append(int(input(str(counter) + ": ")))
    counter += 1
    items -= 1

for x in grade:
    sum = sum + x

print(sum / len(grade))

