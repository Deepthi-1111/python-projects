import random

n = random.randint(1,100)

while True :
    try:
        a = int(input('your guess :'))
        if a < n :
            print("too low")
        elif a > n:
            print("high")
        else :
            print("correct")
            break
    except ValueError:
        print('invalid')

    
