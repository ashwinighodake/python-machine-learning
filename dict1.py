def main():
    fess = [12000,15000,12500,15500]
    print(fess)

    print("Please enter batch name")
    batch=input()
    print("Your entered batch nname is ",batch)

    if batch=="PPA":
        print("fees are:",fess[1])
    elif batch=="Python":
        print("fees are:",fess[0])
    elif batch=="LSP":
        print("Fees are:",fess[2])
    elif batch=="Angular":
        print("Fees are:",fess[3])
    else:
        print("There is no such batch")
        
if __name__=="__main__":
    main()