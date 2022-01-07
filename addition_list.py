#1.Write a program which accept N numbers from user and store it into List. Return addition of all
#elements from that List.
#Input : Number of elements : 6
#Input Elements : 13 5 45 7 4 56
#Output : 130

def Addition(data):
    sum=0
    for i in range(len(data)):
        sum=sum+data[i]

    return sum

def main():
    print("Enter number of elements in the list:")
    no=int(input())

    data=[]
    print("Enter the elements in the list")
    for i in range(no):
        data.insert(i,int(input()))
        
    ret=Addition(data)
    print("Addition of the elements are:",ret)
    
if __name__=="__main__":
    main()

