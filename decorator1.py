def Division(a,b): #0x100
    ans=a/b
    return ans

def SmartDivision(fun_name): #fun
    def Inner(a,b):
        if a<b:
            a,b=b,a
        return fun_name(a,b)
    return Inner

Division=SmartDivision(Division) #first executing line 

def main():
    print("Enter number 1:")
    no1=int(input())
    print("Enter number 2:")
    no2=int(input())

    res=Division(no1,no2)
    print("Division is:",res)
    
if __name__=="__main__":
    main()