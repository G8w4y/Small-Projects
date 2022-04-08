import time

weight = input("Whats your weight in kg?\n")
height = input("Whats your height in m? eg. 1.85\n")

bmi = (float(weight)/((float(height))**2))
print("Your BMI is " + str("{:.1f}".format(bmi)))
time.sleep(1)
if bmi < 18.5:
    print("You are under weight.")
elif bmi >= 18.5 and bmi <= 24.99:
    print("You are of normal weight.")
elif bmi >= 25 and bmi <= 29.99:
    print("You are over weight.")
elif bmi > 30:
    print("You are obese.")
else:print("Please try again")

#Different code below that does mostly the same thing
# import math

# bmi = (float(weight)/((float(height))**2))

# print(str(int(weight)) + " ÷ " + "(" + str(height) + " X " + str(height) + ") = " + str("{:.15f}".format(bmi)))
# print("Your BMI is " + str("{:.1f}".format(bmi)))
# if bmi < 18.5:
#    print("Your BMI is " + str(int(math.ceil(bmi))) + ", " + "you are underweight.")
# elif bmi >= 18.5 and bmi <= 24.99:
#    print("Your BMI is " + str(int(math.ceil(bmi))) + ", " + "you have a normal weight.")
# elif bmi >= 25 and bmi <= 29.99:
#    print("Your BMI is " + str(int(math.ceil(bmi))) + ", " + "you are slightly overweight.")
# elif bmi >= 30 and bmi <= 34.99:
#    print("Your BMI is " + str(int(math.ceil(bmi))) + ", " + "you are obese.")
# elif bmi > 40:
#    print("Your BMI is " + str(int(math.ceil(bmi))) + ", " + "you are clinically obese.")
# else:print("Please try again")