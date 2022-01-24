#5. Write a recursive program which accept number from user and return its
#factorial.
#Input:5
#Output : 120

def Factorial(no):
    if no==0:
        return 1
    if no!=0:
        return no*Factorial(no-1)
def main():
    print("Enter a number:")
    no=int(input())
    ret=Factorial(no)
    print("Factorial is:",ret)

if __name__=="__main__":
    main()