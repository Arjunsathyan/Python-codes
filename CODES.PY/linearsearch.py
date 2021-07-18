def linearsearch(ar,s,item):
    for i in range(0,s):
        if(ar[i]==item):
            return i

    return -1


    


ar=[33,66,1,24,98]
s=len(ar)
x=int(input('Enter the element to be searched for'))
res=linearsearch(ar,s,x)
if(res!=-1):
    print('Element found at position',res)
else:
    print('Element not found')
