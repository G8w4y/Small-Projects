#Creating a tip calculator
print("Welcome to the tip calculator.")
#Total bill size?
bill_size = float(input("What was the total bill? "))
#Number of people to split the bill between?
num_people = int(input("How many people to split the bill? "))
#What percentage tip would you like to give?
tip = int(input("What percentage tip would you like to give? eg. 5, 10, 15: "))
tip_percentage = tip/100
#Each person should pay:
print("Each person should pay")
split_bill = ((bill_size) + (bill_size*tip_percentage))/num_people
print(round(split_bill, 2))