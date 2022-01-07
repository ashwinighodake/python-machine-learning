#3.Write a program which accept N numbers from user and store it into List. Return Minimum
#number from that List.
#Input : Number of elements : 4
#Input Elements : 13 5 45
#Output : 5

def Minimum(data):
    min=data[0]
    for i in range(len(data)):
        if(data[i]<min):
            min=data[i]
    return min

def main():
    print("Enter number of elements in the list:")
    no=int(input())

    data=[]
    print("Enter the elements in the list")
    for i in range(no):
        data.insert(i,int(input()))
        
    ret=Minimum(data)
    print("Min element:",ret)
    
if __name__=="__main__":
    main()

