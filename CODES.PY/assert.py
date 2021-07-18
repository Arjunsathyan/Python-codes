'''assertions are statements that assert or state a fact cofidentially in our program.Assertio are simply boolean expression that checks if conditio return true or false.If it is true it does nothing and move to hte next line else if it is false it stops and raises an error'''

def avg(marks):
   assert len(marks)!=0 ,"List is empty" #prints message along with the error
   return sum(marks)/len(marks)


marks=[11,22,33]
print('averagre of the marks is',avg(marks))
marks=[]
print(avg(marks))       #causes asssertio error


