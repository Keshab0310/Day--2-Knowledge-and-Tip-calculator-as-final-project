#This is one of the example code
two_digit = input("Write two digit number: ")

first_digit = int(two_digit[0]) #converts first character to integer which user had entere 
second_digit = int(two_digit[1]) #converts second character to integer which user had enter
sum = first_digit + second_digit
print("The sum of " + str(first_digit) + " and " + str(second_digit)  + " is " + str(sum))

#Here is another..... way
two_digit = input("Write two digit number: ")

first_digit = int(two_digit[0])
second_digit = int(two_digit[1])
sum = first_digit + second_digit
print (f"The sum of {first_digit} and {second_digit} is {sum}") #f-string is used to print the variables in string and curly brackets ({}) are used to store the value

