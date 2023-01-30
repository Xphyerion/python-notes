print('Body Mass Index')

name = input("Enter your name : ")

mass =float(print('ENter you weight in kg :'))
height_cm = float(input('Enter your height in cm :'))


height_m = height_m** = height_cm *0.01
bmi = weight/height_m

print(f'''
hello {name}
you're weight in kg is : {mass}
you're height in m is : {height_m}
you're BMI is {bmi}
and you are :
''')
if bmi <= 18.5:
    print('Underweight!')
elif bmi > 18.5 and bmi <= 25:
    print('Healthy')
elif bmi > 25 and bmi <=30:
    print('Overweight!')
else:
    print('OBESE!')
    