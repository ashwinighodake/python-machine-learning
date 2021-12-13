#import marvellous
#from marvellous import *
import marvellous as M
import infosystems
def main():
    print("Inside module:",__name__)
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))

    ret=M.Addition(no1,no2)
    print("Addition is",ret)

    ret=infosystems.Substraction(no1,no2)
    print("Substrction is:",ret)

if __name__=="__main__":
    main()