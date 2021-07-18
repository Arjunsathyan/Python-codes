cubes={1:1,2:8,3:9,4:64,5:125}
print(cubes)

#removes all items
cubes.clear()
print(cubes)  #output {}

#creating using comphrehension
squares={x:x*x for x in range(6)} 
for i in squares:
    print(squares[i])


print(squares)


#build in function in dictionary
print(len(squares))
print(sorted(squares))
