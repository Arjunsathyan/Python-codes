'''list1=[1,2,3,4]
list2=list1
print('list1 --->',list1)
print('list2 ___>',list2)
print()
list1.append([5,6])
print('now list2 -->',list2)
'''
import copy #creating a copy using shallow copy

oldlist=[[1,2,3],[4,5,6],[8,9,10]]
newlist=copy.copy(oldlist)
print('old list',oldlist)
print('new list',newlist)

oldlist[1][1]='AA'
print(oldlist)
print(newlist)  #both will have same output
print()
newlist=copy.deepcopy(oldlist)
print('id of oldlist',id(oldlist))
print('id of newlist',id(newlist))
oldlist[2][2]='BB'
print(oldlist)
print(newlist)
