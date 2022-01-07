
def Addition(no):
    sum=0
    for digit in str(no):
        sum+=1
        
    return sum
def main():
    print("Enter a number:")
    no=input()
    ret=Addition(no)
    print("Addtion of the digits are:",ret)

if __name__=="__main__":
    main()