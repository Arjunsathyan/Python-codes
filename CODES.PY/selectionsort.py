def selsort(ar):
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if(ar[i]>ar[j]):
                ar[i],ar[j]=ar[j],ar[i]

ar=[22,5,99,7,1]
selsort(ar)
print("the sorted array is ")
print(ar)
for i in range(len(ar)):
    print(ar[i],end=" ")
