#3.Write a recursive program which display below pattern.
#Input : 5
#Output : 5 4 3 2 1
def Pattern(no):
    if(no>0):
        print(no,end="\t")
        no=no-1
        Pattern(no)
def main():
    Pattern(5)
if __name__=="__main__":
    main()