alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end = False

def encrypt(text, shift):
    encrypted_text = ""
    list_of_words = list(text)
    for i in list_of_words:
        if i in alphabet:
            index_of_letter = alphabet.index(i) + shift
            if index_of_letter > 25:
                index_of_letter -= 26
            new_letter = alphabet[index_of_letter]
            encrypted_text += new_letter
        else:
            encrypted_text += i
    print(f"\nThe encoded text is: {encrypted_text}")

def decode(text, shift):
    encrypted_text = ""
    list_of_words = list(text)
    for i in list_of_words:
        if i in alphabet:
            index_of_letter = alphabet.index(i) - shift
            new_letter = alphabet[index_of_letter]
            encrypted_text += new_letter
        else:
            encrypted_text += i
    print(f"\nThe decoded text is: {encrypted_text}")


import os
import sys


def restart():
    print('\n\nHere we go again...\n\n')

    os.execv(sys.executable, ['python'] + sys.argv)



while not end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decode(text, shift)
    else:
        print("\nYou need to type 'encode' or 'decode'")
        restart()
    end_question = input("Do you want to continue? (y/n):")
    if end_question == "n":
        end = True
    elif end_question == "y": 
        restart()


# if direction == 'encode':
#     encrypt(text, shift)
# elif direction == 'decode':
#     decode(text, shift)
# # else:
# #     print("You need to type 'encode' or 'decode'\n")
# #     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
