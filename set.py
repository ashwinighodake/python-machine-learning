data={10,20,30,40}
mylist=[10,20,30,40]
print("Data type is:",type(data))
print("Length is ",len(data))
print("data from the set:",data)
print("data from the list:",mylist)

#print(data[0])
print("Traversal using loop")
for no in data:
    print(no,end= " ")

data1= {10,20,30,40,10}   #duplicate values are allowed but stored once
print("New set is:",data1)

data2={12,20,30.4,40,"Hello","True"}

print("Data 2 set is:",data2)