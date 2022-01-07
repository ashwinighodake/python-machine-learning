# 8. Write a program which accept one number and display below pattern.
# Input :5
# output:1
#        1 2
#        1 2 3
#        1 2 3 4
#        1 2 3 4 5

def pattern(no):
    for i in range(1,no+1):
        j=1
        while(j<=i):
            print(j,end="\t")
            j=j+1

        print(end="\n")

def main():
    print("Enter a number:")
    value=int(input())
    pattern(value)

if __name__=="__main__":
    main()