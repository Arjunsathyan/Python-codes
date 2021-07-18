def multiplication(num):
    for i in range(1,11):
        yield num*i

a=multiplication(5)
for i in range(1,11):
    print(next(a))
