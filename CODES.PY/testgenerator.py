mylist=[1,2,3,5,6]
def gensquare(lst):
    for num in lst:
        
        lst.append(num **2)

    return lst


res=gensquare(mylist)
print(res)
