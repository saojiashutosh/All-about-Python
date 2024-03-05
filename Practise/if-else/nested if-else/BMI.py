# Write a program that calculates a person's BMI based on their height
# (in meters) and weight (in kilograms). Use the following formula: BMI =
# weight / (height^2). Then, classify the BMI according to the following
# ranges:
# QUESTIONS 38 - 41
# NESTED IF - ELSE
# info@codeanddebug.in Code and Debug codeanddebug.in
# Underweight: BMI less than 18.5
# Normal weight: BMI 18.5 - 24.9
# Overweight: BMI 25 - 29.9
# Obesity: BMI 30 or greater

wei = float(input("Enter weight = "))
hei = float(input("Enter height = "))

bmi = wei/(hei**2)

if(bmi < 18.5) :
    print("underweight")
elif(18.5 <=bmi <= 24.9) :
    print("normal weight")
elif(25 <= bmi <= 29.9) :
    print("overweight")
else : 
    print("obesity")