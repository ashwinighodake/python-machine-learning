from functools import reduce

def main():
    data=[5,7,6,8,4]
    print("Original data:",data)

    #filter(function,list)
    newdata=list(filter(lambda no:(no%2==0),data))
    print("data after filter",newdata)
 
    #filter(function,list)
    increamentdata=list(map(lambda no: no+2,newdata))
    print("data after increment",increamentdata)
    
    #reduce(function,list)
    ret=reduce(lambda a,b:a+b,increamentdata)
    print("Data after reduce",ret)

if __name__=="__main__":
    main()