'''regular expression allow to locate and change strings in a very powerful way
They work in almist exactly the same way in every programmung language as well'''
''' Regular expression are used to 
    1: search for an specific string in a large amount of data
    2:Verify that a string has the proper format(phone,email)
    3:Find a string and replace it with another string
    4:Format data into thr proper form for importing examples'''

    #importing regex module
import re
if re.search('arjun','hello my name is arjun'):
    print('found the name')

mystr=re.findall("ape.","The ape was at the apex")#findall returns list of matches
for i in mystr:
    print(i)
print()
print()
thestr='the ape was at the apex'
for i in re.finditer('ape.',thestr):

    startend=i.span()  #span returns the location of string

    print(startend)

    print(thestr[startend[0]:startend[1]])
