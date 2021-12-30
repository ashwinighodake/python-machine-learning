import arithmatic as A

def main():
    print("Enter First number:")
    value1=int(input())

    print("Enter Second number:")
    value2=int(input())
 
    ret=A.Addition(value1,value2)
    print("Addition of the given numbers are:",ret)

    ret=A.Substraction(value1,value2)
    print("Substraction of the given numbers are:",ret)

    ret=A.Multiplication(value1,value2)
    print("Multiplication of the given numbers is:",ret)

    ret=A.Division(value1,value2)
    print("Division is:",ret)

if __name__=="__main__":
    main()