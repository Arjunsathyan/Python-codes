people={ 1:{'name':'Arjun','age':20,'sex':'M','dep':'junior Dev'},2:{'name':'Amal','age':20,'sex':'M','dep':'jumior dev'}}
#print(people)
people[3]={'name':'Levi','age':24,'sex':'M','dep':'scout regiment'} #adding key value in dictionary
print(people)
del people[2]['dep']
print('\n',people)
print(people.items())  #iterating through dictionary
