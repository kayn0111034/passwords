import collections
import string
import random

def password_gen(char_amount):
    letters=collections.deque(string.ascii_letters)
    numbers=collections.deque(string.digits)
    characters=collections.deque(letters+numbers)

    password=[]

    for i in range(letter_amount):
        p=random.choice(characters)
        password.append(p)

    password=''.join(password)
    print(password)

def password_with_num_gen(char_amount, number_amount):
    letters=collections.deque(string.ascii_letters)
    numbers=collections.deque(string.digits)

    password=[]
    pass_num=[]
    counter=0

    for i in range(int(char_amount-number_amount)):

        password_letters=random.choice(letters)
        password.append(password_letters)

    for i in range(number_amount):
        password_numbers=random.choice(numbers)
        pass_num.append(password_numbers)

        password.insert(random.randint(0,char_amount),pass_num[counter])

        counter+=1
#single line comment changes color of print and function for some reason


    password=''.join(password)
    print(password)
