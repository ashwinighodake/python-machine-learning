# Write a program which accept one number from user and return its factorial.
# Input :5
# Output : 120

def Fact(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i

    return fact

def main():
    print("Enter a number:")
    value=int(input())

    ret=Fact(value)
    print("Factorial of given number is:",ret)

if __name__=="__main__":
    main()