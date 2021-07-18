def bubblesort(ar,s):
    
    for i in range(s-1):
        for j in range(0,s-1-i):
            if(ar[j]>ar[j+1]):
                ar[j],ar[j+1]=ar[j+1],ar[j]

    print(ar)






ar=[34,28,45,5,1]
s=len(ar)
bubblesort(ar,s)
