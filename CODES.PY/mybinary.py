def binary(arr,s,item):
    beg=0
    last=s-1
    while(beg<=last):
        mid=(beg + last)//2

        if(arr[mid]==item):
            return mid

        elif(item>ar[mid]):
            beg=mid +1

        else:
            last=mid-1


arr=(2,4,7,88,99)
s=len(arr)
item=int(input('Enter the element to be found'))
print('element found at',binary(arr,s,item))
