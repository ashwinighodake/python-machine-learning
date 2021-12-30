
def addition(no):
    mid=no/2
    i=1
    sum=0

    while(i<=mid):
        if(no%i==0):
            sum=sum+i
        i=i+1
    return sum
def main():
    print("Enter number:")
    value=int(input())

    ret=addition(value)
    print("Addition is:",ret)

if __name__ =="__main__":
    main()