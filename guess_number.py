import random
rand_number=random.randint(1,250)
user_number=0
while(user_number!=rand_number):
    user_number=int (input("enter the number: "))
    if user_number>rand_number:
        print ("you need to guess a lower number:")
    elif user_number<rand_number:
        print("you need to guess a higher number:")
    elif user_number==rand_number:
        print ("congratulation! you guesed the number:")
    else:
        print("invalid input")