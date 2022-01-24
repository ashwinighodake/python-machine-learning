def Outer():
    print("Inside Outer function")
    
    def Inner():
        print("Inside Inner Function")
    
    Inner()
def main():
    Outer()

if __name__=="__main__":
    main()