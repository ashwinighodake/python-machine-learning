
def Fun(*value):    #variadic arguments =means any number of arguments are there,data type is tuple so it is non modifiable
    sum=0
    for no in value:
        sum=sum+no
    return sum

def main():
    ret=Fun(10,20,30,40,50)
    print("Addition is",ret)

    ret=Fun(10,20,30,40)
    print("Addition is",ret)

    ret=Fun(100,20,30,40,50)
    print("Addition is",ret)

    ret=Fun()
    print("Addition is",ret)


if __name__=="__main__":
    main()