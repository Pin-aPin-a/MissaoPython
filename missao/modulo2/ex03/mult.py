#!/usr/bin/env python3

first_number: int
second_number: int
first_number = int(input ("Enter the first number: "))  
second_number = int (input("Enter the second number: ")) 
multiplicacao = first_number * second_number
print (str(first_number) + "x" + str(second_number)+ "=" + str (multiplicacao)) 
if multiplicacao > 0 : 
    print ("The result is positive.") 
elif multiplicacao < 0 :
    print ("The result is negative.")
else:
    print ("The result is positive and negative.") 
