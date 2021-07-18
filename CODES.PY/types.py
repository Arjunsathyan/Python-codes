from __future__ import print_function
num_int=333
num_float=122.577

num_new=num_int+num_float
print('num_int =',type(num_int))
print('num_float',type(num_float))
print('sum of two',type(num_new))
print('int value',int(num_new)) #returns integer value

num=145.55
print("type",type(num))
print(isinstance(num,int))  #returns boolean values 
print(isinstance(num,float))

complex_num=50 + 60j
print(type(complex_num))
print(isinstance(complex_num,complex))

print(0b111001)   #returns the binary of the corresponding number
print(0xAB)       #returne hexadecimal coorespondance
print(0o34)        #returns octal correspondence

print(0.1+0.2)

from decimal import Decimal as D   #removes the garbage values due to the software
print(D('0.1') + D('0.2'))

import random 

for i in range(5):                           #prints random numbers
    print(random.randrange(1,100))
