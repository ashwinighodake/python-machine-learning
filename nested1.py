def Outer():
    print("Inside Outer function")
    
    def Inner():
        print("Inside Inner Function")
    
    return Inner    #return hashcode
def main():
    func_name=Outer()       #it call to the outer function
    func_name()            #it call to the inner function

if __name__=="__main__":
    main()