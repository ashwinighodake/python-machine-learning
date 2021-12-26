import array as ARR

def main():
      data=ARR.array('i',[10,20,30,40]) # i=int data=10,20,30,40 all data homogenous
      print(data)
      print("length of array is",len(data))
      print("type of array is:",type(data))
      print(data[0])
      print(data[1])

      print("data from array")
      for i in range(len(data)):
          print(data[i])
      print("using while loop")
      i=0
      while(i<len(data)):
          print(data[i])
          i=i+1
    
      print("Using second loop")
      for no in data:
          print(no,end="\t")

if __name__=="__main__":
    main()