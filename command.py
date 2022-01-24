#import sys
from sys import *
def main():
    print("number of command line arguments are:",(len(argv)))
    print("Nameof application is:",argv[0])
    
    for data in argv:
        print(data)


if __name__=="__main__":
    main()