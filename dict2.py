def main():
#    fess = [12000,15000,12500,15500]
 
    fees = {"python":12500,"PPA":15000,"LSP":20000,"Angular":15000}

    print(fees)
    print("Please enter batch name")
    batch=input()

    print("fees are:",fees[batch])    
if __name__=="__main__":
    main()