import Marvellous_add

def main():
    print("Enter how many elements you want to insert:");
    size=int(input())
    
    Data=[]
    print("Enter the elements:")

    for i in range(size):
        Data.append(int(input()))

    print(Data)

    ans=Marvellous_add.Addition(Data)

    print(ans)

if __name__=="__main__":
    main()