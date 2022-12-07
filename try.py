test = False
while test == False:
  try:
    age = int(input('Enter your age: '))

    faveNum = int(input('What is your favorite number: '))

    if age <= 21:
      print('You are not allowed to enter, you are too young.')
      test = True
    else:
      print('Welcome, you are old enough.')
      test = True
  except:
      print("You may have added a letter by accident, try")


try:
    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except:
    print("Fun Fact! Your age divided by your favorite number is undefined.")
