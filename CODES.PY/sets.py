arr={ 1, 2, 4, 6 ,99 }
lis=[ 90, 44, 5]
s=set(lis)
print(s)
arr.update([20,40,50], [100, 7, 9])
print(arr)
arr.remove(100)
arr.discard(9)
print(arr)
print(arr.union(s))
print(arr | s)
print(arr & s)

