li1 = []
li2 = [3,4,5]
li4 = list(range(1,11))
li3 = list ((1,2,3))
li5 = list (range(3))

print(li1 , li2 , li3 , li4, li5)

print(list(filter(lambda x: x %2 ==1, range(1,20) )))  # odd number list 

print([x ** 2 for x in range (1,11) if x %2 ==1]) # sqauare root of odd numbers

print([x for x in [3, 4, 5, 6, 7] if x > 5 ])

print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))