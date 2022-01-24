#2. Write a recursive program which display below pattern.
#Input : 5
#Output : 1 2 3 4 5
def Pattern(no,i):
    if(no>0):
        print(i,end="\t")
        no=no-1
        i=i+1
        Pattern(no,i)
def main():
    Pattern(5,1)
if __name__=="__main__":
    main()