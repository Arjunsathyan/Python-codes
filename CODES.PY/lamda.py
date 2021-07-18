'''a=lambda x:x**2
b=int(input('Enter the number'))
print('double of{0} the number is{1}'.format(b,a(b)))'''

mlist=[1,2,3,4,5,6,7,8]
newlist=list(filter(lambda x: (x%2==0),mlist))
print(newlist)

newlist=list(map(lambda x:x*2,newlist))
print(newlist)
