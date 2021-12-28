from functools import reduce

def ChkEven(no):     # def ChkEven(no): return(no%2==0)
    if(no%2== 0):
        return True
    else:
        return False

def Increament(no):
    return no+2

def Addition(a,b):
    return a+b

def main():
    data=[5,7,6,8,4]
    print("Original data:",data)

    #filter(function,list)
    newdata=list(filter(ChkEven,data))
    print("data after filter",newdata)
 
    #filter(function,list)
    increamentdata=list(map(Increament,newdata))
    print("data after increment",increamentdata)
    
    #reduce(function,list)
    ret=reduce(Addition,increamentdata)
    print("Data after reduce",ret)

if __name__=="__main__":
    main()