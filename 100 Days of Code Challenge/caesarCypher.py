def caesar(option,text,shiftAmount):
    alphabet = "abcdefghijklmnopqrstuvwxyzæøå"
    alphabetList = list(alphabet)
    shift = int(shiftAmount)
    letterCount = 0
    processed_text = []
    text_to_process = list(str(text).lower())
    length_of_text = len(text)

    if option == "-e":
        alphabetList_shifted = alphabetList[shift:] + alphabetList[:shift]
    elif option == "-d":
        alphabetList_shifted = alphabetList[(shift*-1):] + alphabetList[:(shift*-1)]

    while letterCount < length_of_text:

        for everyletter in range(0,len(alphabetList)):
            if letterCount == length_of_text:
                break
            elif text[letterCount] == " ":
                processed_text += " "
                letterCount += 1
            elif alphabetList[everyletter] == text_to_process[letterCount]:
                processed_text += alphabetList_shifted[everyletter]
                letterCount += 1
    print(''.join(processed_text))

keep_going = True

while keep_going:

    not_quit = input("Press 1 to continue encrypting/decrypting and 0 (zero) to quit.\n").lower()
    if "0" in not_quit:
        keep_going = False
    elif "1" in not_quit:
        optionChoice = input("Please type -e to Encrypt or -d to Decrypt\n").lower()
        inputText = input("Please input text to process.\n").lower()
        inputShift = input("Please input shift amount.\n")
        caesar(option = optionChoice, text = inputText, shiftAmount = inputShift)




######## Tidligere CaesarCypherCode hvor mye var repetert ##############

# def encrypt():
#     #from collections import deque
#     alphabet = "abcdefghijklmnopqrstuvwxyzæøå"
#     alphabetList = list(alphabet)

#     print(alphabetList)
#     print(type(alphabetList))

#     word_to_encrypt = list(input("What's the word you wan't to encrypt?\n").lower())
#     length_of_word_to_encrypt = len(word_to_encrypt)
#     shift = int(input("How far you want to shift it?\n"))

    

#     alphabetList_shifted = alphabetList[shift:] + alphabetList[:shift]
#     #print(alphabetList_shifted)
#     word_encrypted = []
#     letter_count = 0
#     while letter_count < length_of_word_to_encrypt:

#         for everyletter in range(0,len(alphabetList)):
#             if letter_count == len(word_to_encrypt):
#                 break
#             elif word_to_encrypt[letter_count] == " ":
#                 word_encrypted += " "
#                 letter_count += 1
#             elif alphabetList[everyletter] == word_to_encrypt[letter_count]:
#                 word_encrypted += alphabetList_shifted[everyletter]
#                 letter_count += 1
    
#     print(''.join(word_encrypted))

# def decrypt():
#     alphabet = "abcdefghijklmnopqrstuvwxyzæøå"
#     alphabetList = list(alphabet)

#     word_to_decrypt = list(input("What's the word you wan't to decrypt?\n").lower())
#     length_of_word_to_decrypt = len(word_to_decrypt)
#     shift_back = (int(input("How far has the word been shifted?\n")))*(-1)
    
#     alphabetList_shifted = alphabetList[shift_back:] + alphabetList[:shift_back]
#     #print(alphabetList_shifted)
#     word_decrypted = []
#     letter_count = 0
#     while letter_count < length_of_word_to_decrypt:

#         for everyletter in range(0,len(alphabetList)):
#             if letter_count == len(word_to_decrypt):
#                 break
#             elif word_to_decrypt[letter_count] == " ":
#                 word_decrypted += " "
#                 letter_count += 1
#             elif alphabetList[everyletter] == word_to_decrypt[letter_count]:
#                 word_decrypted += alphabetList_shifted[everyletter]
#                 letter_count += 1
#     print(''.join(word_decrypted))
    




# keep_going = True

# while keep_going:

#     not_quit = input("Press 1 to continue encrypting/decrypting and 0 (zero) to quit.\n").lower()
#     if "0" in not_quit:
#         keep_going = False
#     elif "1" in not_quit:
#         en_or_de_crypt = input("Encrypt or decrypt?\n").lower()
#         if "d" in en_or_de_crypt:
#             decrypt()
#         else:
#             encrypt()