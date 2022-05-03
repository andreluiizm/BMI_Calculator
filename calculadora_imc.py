#   ASK THE USER'S NAME AND WELCOME
name = input("What's your name? ")
answer = input(f"Hello {name}, Welcome! Let's ask some questions to know your BMI, Ok? ")

#   COLLECTING INFORMATION: AGE, WEIGHT (KGS and LBS), HEIGHT (MT and INC)
age = int(input('How old are you? '))
weight_un = input('Which unit of weight do you prefer? 1 - Kilograms or 2 - Pounds ')
height_un = (input('Wich unit of height do you prefer?? 1 - Meters or 2 - Inches '))


if weight_un == '1':
    weight_kg = float(input("What's your weight? "))

else:
    weight_lbs = float(input("What's your weight? "))

    
if height_un == '1':
    height_meters = float(input("What's your height? "))

else:
    height_inches = float(input("What's your height? "))



     #   IBM CALCULATOR VARIABLES

if weight_un == '1' and height_un == '1':
    bmi_kg_mt = weight_kg / (height_meters**2)

else:
    bmi_lbs_in = weight_lbs*703 / (height_inches * height_inches)



#    SHOW THE RESULTS
print(f'Name: {name}')
print(f'Age: {age} years')

if weight_un == '1' and height_un == '1':
    print(f'Your BMI is: {bmi_kg_mt:.2f}')

else:
    print(f'Your BMI is: {bmi_lbs_in:.2f}')


#    CONDITIONS TO SHOW THE DIAGNOSTIC
if bmi_kg_mt < 18.5 or bmi_lbs_in < 18.5:
    print('Classification: Underweight')
    print('Health Risk: Minimal')

elif bmi_kg_mt == 18.5 or bmi_kg_mt <= 24.9 or bmi_lbs_in == 18.5 or bmi_lbs_in <= 24.9:
    print('Classification: Normal Weight')
    print('Health Risk: Minimal')

elif bmi_kg_mt == 25.0 or bmi_kg_mt <= 29.9 or bmi_lbs_in == 25.0 or bmi_lbs_in <= 29.9:
    print('Classification: Overweight')
    print('Health Risk: Increased!!')

elif bmi_kg_mt == 30.0 or bmi_kg_mt <= 39.9 or bmi_lbs_in == 30.0 or bmi_lbs_in <= 34.9:
    print('Classification: Obese')
    print('Health Risk: High!!!!!')

elif bmi_lbs_in == 35 or bmi_lbs_in <= 39.9:
    print('Classification: Severely Obese')
    print('Health Risk: Very High!!!!!')

elif bmi_kg_mt > 40 or bmi_lbs_in > 40:
    print('Classification: Morbidly Obese')
    print('Health Risk: Extremely High!!!!!')

