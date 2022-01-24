from sys import *
def Addition(value1,value2):
    ans=value1+value2
    return ans

def main():
    print("------------------Marvellous Infosystem:Automation 1------------")
    print("Script name:",argv[0])
    print("Number of arguments Accepted",len(argv)-1)
   
    if(len(argv)==1):
      if(len(argv)>3 or len(argv)<2):
          print("Invalid Arguments")
          print("Use -u for usage")
          print("Use -h for help")
          exit()
    if(len(argv)==2):
      if(argv[1]=='-u' or argv[1]=='-U'):
          print("Usage: Script is used to perform the addition of 2 numbers ")
          exit()

      elif(argv[1]=='-h' or argv[1]=='-H'):
        print("Help : Name_of_Script First_Argument Second_Argument")
        exit()
      else:
         print("There is no such flag")

    if(len(argv)==3):
       try:
          iRet=Addition(int(argv[1]),int(argv[2]))
          print("Addition is:",iRet)
       
       except Exception:
        print("Exception while executing the script")
        print("Please check the input or contact the developer")

if __name__=="__main__":
    main()