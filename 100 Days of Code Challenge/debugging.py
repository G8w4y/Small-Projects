# def my_function():
#     for i in range(1, 21):
#         #print(i)
#         if i == 20:
#             print("You got it")

# my_function()

# from random import randint

# dice_imgs = ["1","2","3","4","5","6"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])

# year = int(input("Whats your year of birth?"))
# if year >= 1980 and year <= 1994:
#     print("Your a millennial.")
# elif year > 1994:
#     print("You are Gen Z.")

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

def mutate(a_list):
    b_list = []
    for item in a_list:
        #new_item = a_list*[item] * 2
        new_item = item * 2
        print(new_item)
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])