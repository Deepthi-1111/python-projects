def inputval () :
    num1 = int(input("enter first number :"))
    num2 = int(input("enter second number :"))
    exp = input('enter the operation :')
    return num1 , num2 , exp

#inputval()
n1 , n2 , expo = inputval()
result = 0
if expo == '+' :
    result = (n1 + n2)
elif expo == '-' :
    result = (n1 - n2)
elif expo == '*' :
    result = (n1 * n2)
elif expo == '/' :
    result = (n1 / n2)
else :
    print('invalid symbol')

print(result)


