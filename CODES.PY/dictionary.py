mydict={1:"Bucky",2:"Falcon",3:"Zemo"}
#print(mydict[2])
#print(mydict[3])
mydict[4]="jhon walker"
#print(mydict)
mydict[4]="steve"
print(mydict)
mydict[5]="jhon  walker"
mydict[6]="cross bones"
print(mydict)
#mydict.pop()
#print(mydict)
record={"n":"Arjun","age":20,"dep":"Developer"}
print(record)
print(record["n"]);

# To input a dictionary 
d = {}
n = input("Enter number of key-value pairs/ elements you want in your dictionary")
while n>0:
  k = input("enter the key")
  v = input("enter the value")
  d[k] = v 
  n = n-1 
print(d[k])
