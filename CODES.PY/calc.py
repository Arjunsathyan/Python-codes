def addition(num1,num2):
    return int(num1) + int(num2)

def subtraction(num1,num2):
    return int(num1) - int(num2)

def multiplication(num1,num2):
    return int(num1) * int(num2)

def division(num1,num2):
    return int(num1) / int(num2)

def choice():
    print('1: ADDITION')
    print('2:SUBTRACTION')
    print('3:MULTIPLICATION')
    print('4:DIVISION')
    ch=int(input('Enter your choice'))
    return ch

def calculation():
    print('enter the choice')
    ch=choice()
    num1=input()
    num2=input()
    if ch==1:
       print('the sum is', addition(num1,num2))
    else:
        print('the sum of the number is',subtraction(num1,num2))

calculation()
