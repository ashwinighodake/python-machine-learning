def Division(a,b):
    ans=a/b
    return ans

def main():
    print("Enter number 1:")
    no1=int(input())
    print("Enter number 2:")
    no2=int(input())

    res=Division(no1,no2)
    print("Division is:",res)
    
if __name__=="__main__":
    main()