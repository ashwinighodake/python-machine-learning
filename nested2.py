def Fun():
    print("Inside Fun")

def Gun(fun_name):   # here hash code of fun function passing as parameter(memory address)
    print("Inside Gun")
    fun_name()

def main():
    Gun(Fun)

if __name__=="__main__":
    main()