def insertionsort(ar,s):
    key=0
    for i in range(1,s):
        key=ar[i]
        j=i-1
        while(j>=0 and ar[j]>key):      
                                
            ar[j+1]=ar[j]                   
            j=j-1
            ar[j+1]=key

    print(ar)


ar=[33,9,44,5,99]
s=len(ar)
insertionsort(ar,s)
