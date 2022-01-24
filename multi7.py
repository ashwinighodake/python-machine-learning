import os
import multiprocessing 

def Square(No):
    print("PID is:",os.getpid())
    return No*No

def main():
    data=[5,3,2,1]
    result=list()

    for i in range(len(data)):
        result.append(Square(data[i]))
    
    print("Result is:",result)

if __name__=="__main__":
     main()