import random

e = {'r':'🪨','p' : '📃','s':'✂️'}

while True:
    
    user = input('enter the input :').lower()
    if user != ('r' or 'p' or 's') :
        print("invalid input , try again ")

    comp = random.choice(('r','p','s'))
    print(f'computer choose ',{e[comp]})
    if user == 'r':
        if comp =='r':
            print("same ")
        elif comp =='p':
            print("you lose")
        elif comp == 's':
            print("you win")

    if user == 'p':
        if comp =='p':
            print("same ")
        elif comp =='s':
            print("you lose")
        elif comp == 'r':
            print("you win")
        break

    if user == 's':
        if comp =='s':
            print("same ")
        elif comp =='r':
            print("you lose")
        elif comp == 'p':
            print("you win")

    b = input('y/n : ')
    if b == 'n':
        break
    else:
        continue

    break
