#write a program which accept one number & display below pattern
# Input:5
# Output: * * * * *
#         * * * *
#         * * *
#         * *
#         * 


def pattern(no):
    for i in range(no,0,-1):
        j=i
        while(j>0):
            print("*",end="\t")
            j=j-1

        print(end="\n")


def main():
    print("Enter a number:")
    value=int(input())
    pattern(value)

if __name__=="__main__":
    main()