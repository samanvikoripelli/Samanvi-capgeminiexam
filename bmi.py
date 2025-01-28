weight = float(input("enter your weight"))
height = float(input("enter your height"))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal"
else:
    category = "obese"
print(f"your BMI is {bmi:.2f} ")
print(f"you are {category}")
