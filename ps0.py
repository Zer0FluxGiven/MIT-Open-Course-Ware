# Solution for Problem Set 0, MIT-OCW 6.0001 - "Into to Computer Science and Programing in Python" 

#Written by Andrew Murphy, 2020

import math

#Here we accept an input from the keyboard, if the input is not a number, the program will regect it
while True:
    try:
        x = float(input('Enter X: \n'))
        break
    except ValueError :
        print('Invalid Entry. Please try again.')

while True:
    try:
        y = float(input('Enter Y: \n'))
        break
    except ValueError :
        print('Invalid Entry. Please try again.')       
 
#Take the log of each number 
log_x = math.log(x)/math.log(2)
log_y = math.log(y)/math.log(2)

#Print the Result
print ( 'x ** y =' , x**y , '\n' , 'Log x, base 2 = ' , log_x , '\n' , 'Log y, base 2 =' , log_y)