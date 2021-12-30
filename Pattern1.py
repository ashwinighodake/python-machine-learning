#2. Write a program which accept one number and display below pattern.
#Input :5
#Output : * * * * *
#         * * * * *
#         * * * * *
#         * * * * *
#         * * * * *

def Pattern(no):

    for i in range(no):
        for j in range(no):
            print("*",end="\t")

        print(end="\n")

def main():
    print("Enter a number")
    value=int(input())

    Pattern(value)

if __name__=="__main__":
    main()