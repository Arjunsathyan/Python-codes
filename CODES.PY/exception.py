'''try:
    a= 100
    b= 0
    c= a/b
    #print('{} / {} ={}'.format(a,b,c))
except ZeroDivisionError:
    print('division not possoble by 0')
try:i
    a=int(input('enter the first number'))
    b=int(input('enter the second number'))
    if(b==0):
        raise TypeError
    c=a/b
    prnt('{} / {} ={}'.format(a,b,c))
except NameError:
    print(' no sorry ath nadakilla,print poi sekkey')
except TypeError:
    print(' second number is zero')'''
class VotersEligibility(Exception):
    def __init__(self):
        super()


try:
    age=12
    if(age<18):
        raise VotersEligibility
except VotersEligibility:
    print('age is less than 18')
else:
    print('age is greater than 18')
finally:
    print('end of program')

