year = int(input("Which year do yo uwant to check?\n"))

leap = "Leap year"
noLeap = "Not a leap year"

if year % 4 != 0:
    print("{}".format(noLeap))
elif year % 100 != 0:
    print("{}".format(leap))
elif year % 400 == 0:
    print("{}".format(leap))
else: print("{}".format(noLeap))

# eller koden under gjΓΈr det samme

# π¨ Don't change the code below π
year = int(input("Which year do you want to check? "))
# π¨ Don't change the code above π

#Write your code below this line π
if int(year) % 4 == 0 or int(year) % 400 == 0:
    print("Leap year.")
else: print("Not leap year.")


#print(1989/4)