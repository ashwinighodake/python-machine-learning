#tuple
#hetergenous
#indexed
#sequential
#ordered
#data of tuple is immutable
data=(10,20,30,40,"Marvellous",10)

print(type(data))

print(data)
print("0th element is:",data[0])
print("Element at 3rd index",data[3])
print("Last element",data[-1])

#data[0]=11
data.append(22)

print("Updated data is:",data)
