    

# i = 0
# while i < 11: 
#     print(i)
#     i = i + 1
    
# print("I can count to ten!")


# mylist = [
#     "grass",
#     "electric",
#     "fire",
#     "water",
#     "dragon"
# ]

# print(range(10))

# for i in (range(1, 10)):
#     print(i)


counter = 0
todos = [""]
prompt = input("Do you want to make a to-do list? Yes or No: ")
while True:
    if prompt == "No":
        break
    elif prompt == "Yes":
        while todos[counter] != "(end)":
            counter += 1
            todos.append(input(str(counter) + ": "))
    else:
        print("Invalid Answer")
        prompt = input("Do you want to make a to-do list? Yes or No: ")

