class Demo:
    A=20    
   
    def __init__(self):
        self.B=30
    def fun(self):  # istance method
        print("Inside instance method")

    @classmethod
    def gun(cls):   #class method
        print("Inside class method")

def main():
    print("Value of the variable ",Demo.A)
    Demo.gun()

    obj1=Demo()
    print("value of instance variable",obj1.B)
    obj1.fun()

if __name__=="__main__":
    main()