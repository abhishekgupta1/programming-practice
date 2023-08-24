def funtiontest1():
    print("hello")
    
funtiontest1()
    
    
def varargs(*args):
    return args

print(varargs(1, 2, 3))

    
    
def keyword_args(**kwargs):
    return kwargs

# => {"big": "foot", "loch": "ness"}
keyword_args(big='foot', loch='ness')


def swap(x, y):
    return y, x

x = 1
y = 2
x, y = swap(x, y)    # => x = 2, y = 1

print("--------------------------")
# => True
print((lambda x: x > 2)(4))

# => 5
print((lambda x, y: x ** 2 + y ** 2)(2, 1))