#30. [Interactive Coding Exercise] BMI 2.0
#==>

bmi = 22
#round function round the nearest whole number
if bmi < 18.5:
  print(f"Your BMI is {bmi}, Your are under weight")
elif bmi < 25:
  print(f"Your BMI is {bmi}, You have normal weight")
elif bmi < 30:
  print(f"Your BMI is {bmi}, You have slightly overweight")
elif bmi < 35:
  print(f"Your BMI is {bmi}, You have obese weight")
else:
  print(f"Your BMI is {bmi}, you have clinically obese")
  
  
#or
#--

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2
#round function round the nearest whole number
if bmi < 18.5:
  print(f"Your BMI is {bmi}, Your are under weight")
elif bmi < 25:
  print(f"Your BMI is {bmi}, You have normal weight")
elif bmi < 30:
  print(f"Your BMI is {bmi}, You have slightly overweight")
elif bmi < 35:
  print(f"Your BMI is {bmi}, You have obese weight")
else:
  print(f"Your BMI is {bmi}, you have clinically obese")