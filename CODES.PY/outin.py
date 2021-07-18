def outerfun():

    def innerfun():
        print('inner function executing')

    return innerfun()


a=outerfun()
print(a)

