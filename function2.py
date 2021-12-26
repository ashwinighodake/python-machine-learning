#python support call by value

def Addition(No1,No2):
    print("Number 1:",No1,"Number 2:",No2)
    ans = No1+No2
    return ans 

def main():
    print("Enter first number:")
    value1=int(input())

    print("Enter second number:")
    value2=int(input())

    #Positional arguments
    #keyword arguments

    ret=Addition(No1=value1,No2=value2)
    print("Addition is:",ret)

    ret=Addition(No2=value1,No1=value2)
    print("Addition is:",ret)

if __name__=="__main__":
    main()