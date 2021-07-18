import random as r
num= r.randrange(1,20)
print('random number',num)
i=1
while True:
    if i==num:
        print('reached {0} the number going to break the loop'.format(num))
        break
    i +=1
