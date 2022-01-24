import os 
import multiprocessing

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
    process1=multiprocessing.Process(target=Fun,args=(No,))
    process2=multiprocessing.Process(target=Gun,args=(No,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("End of main")
if __name__=="__main__":
    main()