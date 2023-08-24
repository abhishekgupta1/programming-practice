# a_list[start:end]
# a_list[start:end:step]

a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
print(a[2:5])
# print(a[-4,-2])
print(a[1:4])
print(a[:4])
print(a[0:4])
print(a[2:]) 
print(a[2:len(a)])
print(a[:]) # it is equal to print(a)

print(a[0:6:2])
print(a[1:6:2])
print(a[6:0:-2])
print(a[::-1])

# remove
li = [1,2,3]
li.pop() # will remove last element 
del li[0] # remove first element 


odd = [1,2,3]
print(odd)
odd.extend([9,11,13])
print(odd)
odd = [1,3,5]
print(odd)

print(odd + [9,11,13])


li = [3, 1, 3, 2, 5]
print(li.sort())
print(li.reverse())
print(li.count())