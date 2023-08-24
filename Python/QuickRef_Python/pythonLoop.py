primes  = [2,3,5,7]
for prime in primes :
    print(prime)
    
animals = ["dogs","cats","mouse"] 
for i, value in enumerate(animals):
    print (i,value)
    # enemurate() adds counter to an iterable
    # prints 0 dogs 1 cat 2 mouse    
    
x = 0
while x < 4:
    print(x)
    x += 1
    

for i in range(4):
    print(i) # Prints: 0 1 2 3
    print("--------------")

for i in range(4, 8):
    print(i) # Prints: 4 5 6 7
    print("--------------")

for i in range(4, 10, 2):
    print(i) # Prints: 4 6 8
    print("--------------")

words = ['Mon', 'Tue', 'Wed']
nums = [1, 2, 3]
# Use zip to pack into a tuple list
for w, n in zip(words, nums):
    print('%d:%s, ' %(n, w))
    
nums = [60, 70, 30, 110, 90]
for n in nums:
    if n > 100:
        print("%d is bigger than 100" %n)
        break
else:
    print("Not found!")
    
        
    
   