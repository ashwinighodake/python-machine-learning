#Write a program which accept number from user and return addition of digits in that number.
#Input : 5187934
#Output : 37

def Addition(no):
    sum=0
    for digit in str(no):
        sum+=int(digit)
        
    return sum
def main():
    print("Enter a number:")
    no=input()
    ret=Addition(no)
    print("Addtion of the digits are:",ret)

if __name__=="__main__":
    main()