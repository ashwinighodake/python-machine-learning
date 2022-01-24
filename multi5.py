import os 
import threading

def Fun(x):
    print("Inside Fun")
    print("PID of Fun is:",os.getpid())
    print("PPID of Fun is:",os.getppid())
    for i in range(x):
        print("Fun:",i)

def Gun(x):
    print("Inside Gun")
    print("PID of Gun is:",os.getpid())
    print("PPID of Gun is:",os.getppid())
    for i in range(x):
        print("Fun:",i)
    
def main():
    No=5
    print("PID of parent process",os.getpid())
    thread1=threading.Thread(target=Fun,args=(No,))
    thread2=threading.Thread(target=Gun,args=(No,))

    thread1.start()
    thread2.start()

    
    print("End of main")
if __name__=="__main__":
    main()