#4.Write a recursive program which accept number from user and return
#summation of its digits.
#Input : 879
#Output : 24
def Add_Digit(no):

    if(no==0):
        return 0
    return int(no%10+Add_Digit(no/10))
        
        
def main():
    print("Enter a number")
    value=int(input())
    ret=Add_Digit(value)
    print("Addition is",ret)
    
if __name__=="__main__":
    main()