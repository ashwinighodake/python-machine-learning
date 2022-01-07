#Write a program which accept one number and display below pattern.
#Input :5
#Output: 1 2 3 4 5
#        1 2 3 4 5        
#        1 2 3 4 5
#        1 2 3 4 5
#        1 2 3 4 5

def pattern(value):
    i=1
    
    while(i<=value):
        j=1
        while(j<=value):
            print(j,end="\t")
            j=j+1
        print(end="\n")
        i=i+1

def main():
    print("Enter a number:")
    no=int(input())

    pattern(no)

if __name__=="__main__":
    main()