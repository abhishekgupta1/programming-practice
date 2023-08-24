import operator

if __name__ == '__main__':
    print("Hello, World!")

def sum(a,b):
    return a+b
    
if __name__ == "__main__":
    print("hellos")
    Number1 = float(input("Enter 1st Number : "))
    Number2 = float(input("Enter 2nd Number : "))
    Sum = sum(Number1, Number2) 
    print("First Number {0} which is getting added to Second Number {1} giving sum {2}".format(Number1, Number2, Sum))
    print(operator.add(Number1,Number2))
    
    