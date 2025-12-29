#the popular refactoring technique : modularization applied to rock ,paper ,scissor code 

import random

e = {'r':'🪨','p' : '📃','s':'✂️'}
def user_choice ():
    while True:    
        user = input('enter the input :').lower()
        if user not in ('r' , 'p' , 's') :
            print("invalid input , try again ")
            continue
        else :
            return user                

def play(user,comp):
    if user == comp:
        print("same")
    elif (
        (user == 'r' and comp == 's') or 
        (user == 'p' and comp == 'r') or
        (user == 's' and comp == 'p') ):
        print('you win')
    else:
        print('you lose')



while True:
    user_global = user_choice()  # user is declared inside function so this step is to make it global      
    comp = random.choice(('r','p','s'))
    print('you chose :',e[user_global])
    print('computer choose :',e[comp])

    play(user_global ,comp )

    b = input('y/n : ').lower()
    if b == 'n':
        break




