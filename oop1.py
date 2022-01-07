class Demo:
    A=20    #class variable
    B=20    #class variable

    def __init__(self):
        self.C=30            #instance variable           
        self.D=40            #instance variable
    
def main():
    print("Value of A:",Demo.A)
    print("value of B",Demo.B)
    obj1=Demo()
    obj2=Demo()

    print("Value of C from obj1:",obj1.C)
    print("Value of C from obj2:",obj2.C)

if __name__=="__main__":
    main()