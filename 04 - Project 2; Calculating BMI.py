#This Project is done to calculate the BMI of the user
#BMI stands for Body Mass Index which measures the health condition of an individual based on their weight and height.
weight = input ("Write  your weight in kg: ")
height = input("write your height in meters : ")
#Converting the inputs from string to float
weight=float(weight)
height=float(height)
BMI=(weight/(height**2))
print(f"Your Body Mass Index (BMI) is {BMI}kg/m^2")