def generator1():
    n=1
    print('this is printed first')
    yield n

    n +=1
    print('this is printed second')
    yield n

    n +=1
    print('this is printed third')
    yield n

a= generator1()
next(a)
next(a)
next(a)
for item in generator1():
    print(item)
print()
def mygenerator(mystr):
    length=len(mystr)
    for i in range(length-1,-1,-1):
        yield mystr[i]

for char in mygenerator("PYTHON"):
    print(char)
