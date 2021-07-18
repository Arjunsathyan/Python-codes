import re
'''square bracket will maatch any one of the charecters between'''
animalstr='cat rat mat fat pat'
animal=re.findall("[crmpf]at",animalstr)
for i in animal:
    print(i)

print()
new='cat rat mat fat pat'
strnew=re.findall("[^cr]at",new) #^ removes cat and rat
for i in strnew:
    print(i)
