#named function
def Add(a,b):
    return a+b

#lambda function
# lambda parameters:expression
Addx= lambda a,b:a+b

def main():
    ret=Add(10,20)
    print("Addition is: ",ret)

    print(type(Add))

    ret=Addx(10,20)
    print("Addition is:",ret)

    print(lambda a,b:a+b)
 
if __name__=="__main__":
    main()