
a=2
print('id(2)=',id(2)) #id is a function used in python to get the memory address
print('id(a)=',id(a))
a=a+1
print('id(a)=',id(a))
print('id(3)=',id(3))
b=a
print('id(b)=',id(b))

                     ####scope

def outer_function():
    global a
    a=20

    def inner_function():
        global a
        a=30
        print('a=',a)


    inner_function()
    print('a=',a)

a=10
print('a=',a)
outer_function()
print('a=',a)
