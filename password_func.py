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
    insert_ord=0

    for i in range(char_amount-number_amount):

        password_letters=random.choice(letters)
        password.append(password_letters)

    for i in range(number_amount):
        password_numbers=random.choice(numbers)
        pass_num.append(password_numbers)

    for i in range(number_amount):
        password.insert(pass_num[insert_ord],random.randint(0,char_amount))
        #returns TypeError: 'str' object cannot be interpreted as an integer
        insert_ord+=1

    password=''.join(password)
    print(password)
