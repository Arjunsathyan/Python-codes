mylist=[2,5,6,7,8,9]
print(mylist[1])

'''for letters in 'human':
    mylist.append(letters)
print(mylist)

print()
hletters=list(map(lambda x: x,'human'))
print(hletters)'''

numlist= [x for x in range(20) if x%2==0]
print(numlist)
nlsit=[x for x in range(100) if x%2==0 if x%5==0]
print(nlsit)
print()
oddeven=['even' if x%2==0 else 'odd' for x in range(10)]
print(oddeven)
matrix=[[1,2],[3,5],[4,6]]
print(matrix)
transpose=[[ row[i] for row in matrix] for i in range(2)]
print(transpose)
