#Knowing the present age of User
current_age =  int(input("Enter your age: "))
age = int(current_age) #defining variable 'age' as integer data type
#If the User lives up to the age of 90
age_left = 90 - age
weeks_left = age_left * 52
print(f"Hello ! You are {age} years old, and you have {weeks_left} week left until you die")
