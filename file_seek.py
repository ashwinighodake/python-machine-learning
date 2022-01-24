import os 
def main():
    print("Enter the file name that you want to open")
    name=input()

    fd=open(name,"rb")
    print("Current offset is:",fd.tell())
    data=fd.read(2)
    print("Data is",data)
    print("Current offset is :",fd.tell())

    fd.seek(3,1)
    print("Current offset is :",fd.tell())
   
    data=fd.read()
    print(data)
    
if __name__=="__main__":
    main()