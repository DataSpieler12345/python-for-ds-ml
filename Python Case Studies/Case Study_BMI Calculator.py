# getting data
weight = int(input("Enter your height in cm "))
height = float(input("Enter the weight in kg "))

bmi = weight / (height)**2

if bmi < 18.5:
   print("Underweight")
elif bmi >= 18.5 and bmi < 25:
   print("Normal")
elif bmi >=25 and bmi < 30:
   print("Overweight")
elif bmi >= 30:
   print("Obesity")