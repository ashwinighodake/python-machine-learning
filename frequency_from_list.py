#4.Write a program which accept N numbers from user and store it into List. Accept one another
#number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#Output : 3

def Frequency(data,no):
    count=0
    for i in range(len(data)):
        if(data[i]==no):
           count=count+1

    return count

def main():
    print("Enter number of elements in the list:")
    no=int(input())

    data=[]
    print("Enter the elements in the list")
    for i in range(no):
        data.insert(i,int(input()))
    
    print("Enter a element which you want to search:")
    value=int(input())
    ret=Frequency(data,value)
    print("Frequency of given  element is:",ret)
    
if __name__=="__main__":
    main()

