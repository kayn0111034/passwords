from password_func import *

print("(0) Random Password Generator")
print("(1) Random Password Generator but You Can Choose the Amount of Numbers In It")

choose=int(input("Which password generator do you want to use?"))

if choose==0:
    print("Create a randomly generated password!")
    char_amount=int(input("Input how long you would like your password to be:"))

    password_gen(char_amount)

if choose==1:
    print("Create a randomly generated password with amount of numbers")
    char_amount=int(input("Input how long you would like your password to be:"))
    number_amount=int(input("Input how many numbers you would like in your password:"))

    password_with_num_gen(char_amount,number_amount)
