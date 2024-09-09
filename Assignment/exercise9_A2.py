"""
Write a program that calculates the Body Mass Index (BMI) and categorizes it into different weight statuses. 
The formula for BMI is weight / height^2, where weight is in kilograms and height is in meters.

Categories:

Underweight: BMI < 18.5

Normal weight: 18.5 <= BMI < 24.9

Overweight: 25 <= BMI < 29.9

Obesity: BMI >= 30

"""

# find the weight and height to get BMI
weight = float(input("Enter the number of weight: ")) # in kg
height = float(input("Enter the number of height: ")) # in meter

BMI = weight / (height * height)

# categories according to your BMI

if (BMI < 18.5):
    print("Underweight")
elif (BMI >= 18.5 and BMI < 24.9):
    print("Normal weight")
elif (BMI >= 25 and BMI < 29.9):
    print("Overweight")
else:
    print("Obesity")

