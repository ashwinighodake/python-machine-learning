#list
#sequential
#indexed 
#Data is Mutable
#allows duplicate
#Heterogenous

Data=[11,21,51,101,3.14]

print("Data type is",type(Data))
print("Length of list is",len(Data))
print("Actual data is :",Data)

print("Data from 0th index :",11)
print("Data from 3rd index:",Data[3])

Data[0]=12
print(Data[0])

Data.append(111)
print(Data)

Data.insert(2,51)
print(Data)

print(Data[-1])