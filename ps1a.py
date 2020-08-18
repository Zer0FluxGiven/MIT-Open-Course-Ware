# Solution for Problem Set 1a, MIT-OCW 6.0001 - "Into to Computer Science and Programing in Python" 

#Written by Andrew Murphy, 2020

#Get the Total Cost of the Dream Home
def get_cost():
    while True:
        try:
            cost = float(input('Enter cost of Dream Home: \n'))
            break
        except ValueError:
            print('Invalid Entry. Please try again.')
    return cost

#Get the user's annual salary 
def get_salary():
    while True:
        try:
            salary = float(input('Enter your Annual Salary: \n'))
            break
        except ValueError:
            print('Invalid Entry. Please try again.')
    return salary

#Get the percentage of the salary saved each month as a decimal.
def get_savings():
    while True:
        try:
            percentage = float(input('Enter the percentage saved as a decimal: \n'))
            break
        except ValueError:
            print('Invalid Entry. Please try again.')
    return percentage
    

#--------------------------------------------
#
#--------------------------------------------

#Get user inputs 
total_cost = get_cost()
salary = get_salary()
savings_percentage = get_savings()

down_payment = 0.25*total_cost #Down-Payment set to 25% of Total Cost
current_savings = 0.0 #Initial savings 
months = 0 #Initial month
r = 0.01 #Interest rate

#Increment savings over month until down payment is reached
while current_savings < down_payment :
    current_savings += (salary/12)*savings_percentage + current_savings*(r/12) #Add monthly savings (monthly salary * savings percentage) and interest
    months += 1

#Print the result
print('Number of Months:', months)

