def fact(n):
    if n in [0,1]:
        return 1
    else:
        print(n)
        return  n * fact(n-1)

print(fact(4))
'''def fibonacci(n):
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        print(n)

print(fibonacci(7))'''
