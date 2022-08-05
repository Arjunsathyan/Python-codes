#Return function in python is used to terminate the function and assign a value to the function which will be returned upon calling the function 
@gfg_decorator
def hello_decorator():
    print("gfg")

hello_decorator=gfg_decorator(hello_decorator)

