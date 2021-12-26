print("Enter number of elements")
size=int(input())

data = set()   # class constructor not a tuple

for i in range(size):
    print("Enter element no:",i+1)
    no=int(input())
    data.add(no)

print("Data from set is:",data)

print("Data to search:")
value=int(input())

if value in data:
    print("Element is there ")
else:
    print("ther is no such element ")