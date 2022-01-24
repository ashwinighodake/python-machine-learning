import os 

def Fun():
    print("Inside Fun")
    print("PID is:",os.getpid())

def Gun():
    print("Inside Gun")
    print("PID is:",os.getpid())
    
def main():
    print("PID is",os.getpid())
    Fun()
    Gun()
if __name__=="__main__":
    main()