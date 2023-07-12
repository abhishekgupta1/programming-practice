import math

def getAbsolute():
    result = int(input("Please enter a negative number : " ))
    
    return math.fabs(result) 

def Main():
    print(getAbsolute())

if __name__ == "__main__":
    Main()