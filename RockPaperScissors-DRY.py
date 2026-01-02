import random

a = {'r' : 'rock' ,'p' : 'paper' , 's' : 'scissors' }
e = {'rock':'🪨','paper' : '📃','scissors':'✂️'}
choices = tuple(e.keys())
def user_choice ():
    while True:    
        user = input('enter the input :').lower()
        if user not in a :
            print("invalid input , try again ")
            continue
        else :
            return a[user]                

def play(user,comp):
    if user == comp:
        print("same")
    elif (
        (user == 'rock' and comp == 'scissors') or 
        (user == 'paper' and comp == 'rock') or
        (user == 'scissors' and comp == 'paper') ):
        print('you win')
    else:
        print('you lose')

while True:
    user_global = user_choice()              
    comp = random.choice(choices)
    print('you chose :',e[user_global])
    print('computer choose :',e[comp])

    play(user_global ,comp )

    b = input('y/n : ').lower()
    if b == 'n':
        break
