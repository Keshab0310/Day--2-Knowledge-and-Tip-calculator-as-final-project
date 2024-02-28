#This is the final project of day 2 of python cooding
#I am trying to make a simple application for calculating the tip
print("Welcome to the tip Calculator.")
bill = float(input("What was the total  bill? ")) #Converting the input into float
tip = int(input("What percentage tip  would you like to give? 10, 12 or 15? "))  #Converting the input into integer and giving the user options to give the tip percentage
people = int(input("How many people to split the bill? "))  #Converting the input into integer
bill_with_tip = (tip /100 *tip + bill)
total_per_person= (bill_with_tip/(people) )
print(f"Each person should pay: $  {total_per_person}")