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
  
while True:
    user_choice()
                  
    comp = random.choice(('r','p','s'))

    print('you chose :',e[user])
    print('computer choose :',e[comp])

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



    b = input('y/n : ').lower()
    if b == 'n':
        break
