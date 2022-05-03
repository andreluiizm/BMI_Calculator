#   ASK THE USER'S NAME AND WELCOME
name = input("What's your name? ")
answer = input(f"Hello {name}, Welcome! Let's ask some questions to know your BMI, Ok? ")

#   COLLECTING INFORMATION: AGE, WEIGHT (KGS and LBS), HEIGHT (MT and INC)
age = int(input('How old are you? '))
weight_un = int(input('Which unit of weight do you prefer? 1 - Kilograms or 2 - Pounds '))
height_un = int(input('Wich unit of height do you prefer?? 1 - Meters or 2 - Inches '))


weight = float(input("What's your weight? "))
height = float(input("What's your height? "))



     #   IBM CALCULATOR VARIABLES

if (weight_un == 1) and (height_un == 1):
    bmi = weight / (height*height)
else:
    bmi = weight*703 / (height * height)


# CLASSIFY

if bmi <= 18.5:
    rank = 'magreza'
elif bmi > 18.5 and bmi < 25:
    rank = 'saudavel'
elif bmi >= 25 and bmi < 30:
    rank = 'sobrepeso'
elif bmi >= 30 and bmi < 35:
    rank = 'obesidade grau 1'
elif bmi >= 35 and bmi < 40:
    rank = 'obesidade severa grau 2'
else:
    rank = 'gordo baleia saco de areia'


#    SHOW THE RESULTS
print(f'Name: {name}')
print(f'Age: {age} years')
print(f'BMI: {bmi}.')
print(f'Classification: {rank}.')

