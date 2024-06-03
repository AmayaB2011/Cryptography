# ©Amaya Buffier
import random
print("Welcome, this is the Caesar Cipher")
alphabet = "abcdefghijklmnopqrstuvwxyz"
code_list = []

mode = input("Encrypt (e) or Decrypt (d): ")
if mode == "e":
    message = input("What is your secret message? ")
    message = message.lower()
    key = (input("What is your key? "))

    if key == "random":
        key = (int(random.randrange(1, 26)))
        print("Your key is: ")
        print(str(key))
        print("Your message is:")
        print(message)
        print("Your secret message is: ")

        for current_letter in message:
            if current_letter in alphabet:
                position_index = alphabet.index(current_letter)
                new_index = (position_index + (int(key))) % 26
                new_letter = alphabet[new_index]
                code_list.append(new_letter)
            else:
                code_list.append(current_letter)
        print(''.join(code_list))
    else:
        print("Your key is: ")
        print(str(key))
        print("Your message is:")
        print(message)
        print("Your secret message is: ")

        for current_letter in message:
            if current_letter in alphabet:
                position_index = alphabet.index(current_letter)
                new_index = (position_index + (int(key))) % 26
                new_letter = alphabet[new_index]
                code_list.append(new_letter)
            else:
                code_list.append(current_letter)
        print(''.join(code_list))
elif mode == "d":
        message = input("What is your secret message? ")
        message = message.lower()
        key = (input("What is your key? "))

        if key == "random":
            key = (int(random.randrange(1, 26)))
            print("Your key is: ")
            print(str(key))
            print("Your message is:")
            print(message)
            print("Your secret message is: ")

            for current_letter in message:
                if current_letter in alphabet:
                    position_index = alphabet.index(current_letter)
                    new_index = (position_index - (int(key))) % 26
                    new_letter = alphabet[new_index]
                    code_list.append(new_letter)
                else:
                    code_list.append(current_letter)
            print(''.join(code_list))

        else:
            print("Your key is: ")
            print(str(key))
            print("Your message is:")
            print(message)
            print("Your secret message is: ")

            for current_letter in message:
                if current_letter in alphabet:
                    position_index = alphabet.index(current_letter)
                    new_index = (position_index - (int(key))) % 26
                    new_letter = alphabet[new_index]
                    code_list.append(new_letter)
                else:
                    code_list.append(current_letter)
            print(''.join(code_list))
