data = { "Even":[2,4,6,8],"Odd":[1,3,5,7,9],"other":[11.5,22.,33.6]}

print(data["Even"][0])

for keys in data:
    print(keys)
    for i in data[keys]:
        print(i)

print("Data by new for loop")

