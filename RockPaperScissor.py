import random

e = {'r':'🪨','p' : '📃','s':'✂️'}

while True:
    
    user = input('enter the input :').lower()
    if user not in ('r' , 'p' , 's') :
        print("invalid input , try again ")
        continue                #continue so that the input q repeats itself
    comp = random.choice(('r','p','s'))

    print('you chose :',e[user])
    print('computer choose :',e[comp])

    if user == comp:
        print("same")
    elif (
        (user == 'r' and comp == 's') or # here / can be written to move to next line as well instead of ( )  
        (user == 'p' and comp == 'r') or
        (user == 's' and comp == 'p') ):
        print('you win')
    else:
        print('you lose')

    # if user == 'r':
    #     elif comp =='p':
    #         print("you lose")
    #     elif comp == 's':
    #         print("you win")
    # if user == 'p':
    #     elif comp =='s':
    #         print("you lose")
    #     elif comp == 'r':
    #         print("you win")
    # if user == 's':
    #     elif comp =='r':
    #         print("you lose")
    #     elif comp == 'p':
    #         print("you win")

#correct but long format
    
    b = input('y/n : ').lower()
    if b == 'n':
        break
#no need for continue if b = yes as it is done automatically 
