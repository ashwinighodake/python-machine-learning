#encapsulation -> class = characteristics+behaviour 
class Arithmatic: #class definition
    def __init__(self,a,b):   #constructor
        print("Inside init constructor")
        self.no1=a   #charcteristics
        self.no2=b   #characteristics

    def Addition(self):    #behaviour
        ans= self.no1 + self.no2
        return ans

def main():
    print("Enter first number:")
    value1=int(input())

    print("Enter second number:")
    value2=int(input())

    obj=Arithmatic(value1,value2)        #object creation
    ret=obj.Addition()

    print("Addition is:",ret)

if __name__=="__main__":
    main()