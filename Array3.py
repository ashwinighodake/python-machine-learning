import array as ARR

def main():
      data=ARR.array('f',[10.5,20.1,30.4,40.2]) # i=int data=10,20,30,40 all data homogenous
      print(data)
      print("length of array is",len(data))
      print("type of array is:",type(data))
      print(data[0])
      print(data[1])

      print("data from array")
      for i in range(len(data)):
          print(data[i])
     
      print("Typecode of array is:",data.typecode)
      print("Using second loop")
      for no in data:
          print(no,end="\t")

if __name__=="__main__":
    main()