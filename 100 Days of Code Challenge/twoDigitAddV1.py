#scipt that takes inn any two-digit number and prints each number added together
#input two digit number as a string
two_digit_number = input("Type a two digit number: ")

#turn string into integer
num = int(two_digit_number)
#create a list containing every digit seperately
list_of_numbers = [int(a) for a in str(num)]
print(list_of_numbers)
#create a list containing the first digit only
a = list_of_numbers[0]
print(a)
#create a list containing the second digit only
b = list_of_numbers[1]
print(b)
#add digits of both lists together and print the result
print(a+b)
