#default arguments

def Area(radius,PI=3.14):      #non default follows default argument 
    ans=0.0
    ans= PI*radius*radius
    return ans

def main():
    print("Enter radius of circle:")
    value=float(input())

    ret=Area(value)
    print("Area is",ret)

    #ret=Area(value,7.10)
    #print("Area is",ret)

    #ret=Area(PI=7.10,radius=value)
    #print("Area is",ret)


if __name__=="__main__":
    main()