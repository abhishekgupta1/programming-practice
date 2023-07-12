# now as we know any program starts with the main function 

def getInput() :
    result = int (input("Enter your number : "))
    return result

def Main():
    print(getInput())

# now we tell python on the main existance 

if __name__ == "__main__":
    Main()    