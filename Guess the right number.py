# This code is contributed by Rohit kumar Ray from NIT Raipur


import random


while True:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('In this game, You have to guess a number between 1 to 100.')
    print('Start GAME \n*******************')

    rand = random.randint(1,100)

    for i in range(1,11):
        
        print(f'You are choosing {i} th times')
        
        a = int(input('Entre your no between 1 to 100 : '))

        if a in range(1,101):
            print(f'You choosen the numbere : {a}')
        else:
            print('You have choosen INVALID number')
            break
        print('-----------------------------------')
        
        if a < rand :
            print('Please choose higher number')
        elif a > rand :
            print('Please choose lower number')
        elif a == rand :
            print('Congratulation , You choosen the write number')
            break

    user_choice=input("Want to Play again?Yes(Y)/No(N) : ")
    if user_choice=='yes' or user_choice=='Yes' or user_choice=='YES'or user_choice=='y' or user_choice=='Y':
                    continue             
    else:
                    break
        
#This code is totally belogs to me . 

# I am doing a experiment a to puch a particular branch in Github