#2.Write a program which accept N numbers from user and store it into List. Return Maximum
#number from that List.
#Input : Number of elements : 7
#Input Elements : 13 5 45 7 4 56 34
#Output : 56
def Maximum(data):
    max=0
    for i in range(len(data)):
        if(data[i]>max):
            max=data[i]
    return max

def main():
    print("Enter number of elements in the list:")
    no=int(input())

    data=[]
    print("Enter the elements in the list")
    for i in range(no):
        data.insert(i,int(input()))
        
    ret=Maximum(data)
    print("Max element:",ret)
    
if __name__=="__main__":
    main()

