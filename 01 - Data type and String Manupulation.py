#There are various data types and one of them is 
#String
#Here is a simple example
print("Hello"[0]) #This will return 'H' as the output because Programmer  Indexing starts from 0.
print("Keshab"[5])  #This will return 'b' as the output because  index also start from 0 and there are 6 letters wihch makes the last letter in 5th if indexing starts from 0.
print("Python"[-1]) # This will return 'n' as the last character in string "Python".
#Similarly here is another example
print("123"+ "456") #This will print '123456'. as output because  we concatenated two strings using + operator.

#Integer
#here is some  integer examples
print(123 + 345)  # Here the Output will be 467.
#Here is another example to write the number in greater digits
print(123_456_789) # The Output will be 123456789 it is so because '_' is used for separating the digits similarly as (,) in maths.

#Float
#here is the example of float, it basically means that the data types with  decimal points.
2.666666

#Lastly here is another data type 
#Bolean
#It always has 2 values and those are true and false.


#To know any data tyoe we can use tyoe check function
a = 55
print(type(a)) #Here  the output will be <class 'int'> which shows that variable a belongs to int data type.
#here are another  example
b = "keshab"
print(type(b)) #The output will be <class 'str'> which indicates that  b belongs to str data type.
c = 4.5567
print(type(c)) # The output will  be <class 'float'> which show that c belongs to float data type.
d= True
print(type(d)) # The output will be <class 'bool'> which show that  d belongs to bool data type.
#To convert the data type we can  use conversion functions
x = str(55)  
print(x) #Here x becomes a string now.
y = float('55') 
print(y)#Now y  become a float.
