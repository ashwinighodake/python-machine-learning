#1. Write a recursive program which display below pattern.
#Input : 5
#Output : * * * * *

def Pattern(no):
    if(no>0):
        print("*",end="\t")
        no=no-1
        Pattern(no)
def main():
    Pattern(5)
if __name__=="__main__":
    main()