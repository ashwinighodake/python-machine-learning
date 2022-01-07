#a number is prime number if & only if that number is greater than 1 & it is divisible by 1 & number itself
#Write a program which accept one number for user and check whether number is prime or not.
#Input :5
#Output : It is Prime Number

def Check_Prime(value):
    flag=False
    if value>1:
        for i in range(2,value):
            if((value%i)==0):
                flag=True
                break
    
    if(flag==True):
        return True
    else:
        return False

def main():
    print("Enter number:")
    no=int(input())
    ret=Check_Prime(no)
    if(ret==True):
        print("It is not prime number")
    else:
        print("It is  prime number")
if __name__=="__main__":
    main()