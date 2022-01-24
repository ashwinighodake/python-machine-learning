import sys
def Display():
    print("Using for loop")
    for i in range(4):
        print("Marvellous")

def DisplayX():
    print("Using while loop")
    i=0
    while(i<4):
        print("Marvellous")
        i=i+1

def DisplayR(no): # recursion
    if(no>0):
        print("Marvellous")
        no=no-1
        DisplayR(no) # recursive call

def main():
    Display()
    DisplayX()
    print("using recursion")
    DisplayR(4)
    print(sys.getrecursionlimit())
if __name__=="__main__":
    main()