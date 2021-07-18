def hello1():
    print('hello there kutta')
def hello2():
    return 'returning hello '

hello1()
print(hello2())








'''def greetings(name,msg='how are you'):   #default parameteri
    print('hello',name,msg)

greetings('arjun'," how you doing")
greetings('amal')'''

def sumAll(*ar):
    sum=0

    for i in ar:
        sum +=i

    return sum

print('the sum of  numbers is',sumAll(1,3,4,5,7)

