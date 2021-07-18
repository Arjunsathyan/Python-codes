x="global" #global variable can be accessed from anywhere

def functn1():
    global x
    y="local"
    x=x*2
    print(x)
    print(y)

print("Global=",x)
functn1()
print("Global=",x)
def outer():
    x="local"

    def inner():
        nonlocal x
        x="nonlocal"
        print("inner",x)


    inner()
    print("outer",x)
