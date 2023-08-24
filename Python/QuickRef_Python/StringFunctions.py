hello = "hello world"
hello = 'hello world'
multi_string = """multiString String lorem ipsum"""

x = 1
y = 2.8 
z = 1J

print(type(x))

my_bool = True
print(my_bool)
my_bool = False
print(my_bool)

print(bool(0)) 
print(bool(1))

list1 = ["apple","banna"]
list2 = [True,False,False]
list3 = [1,2,3,4,5]
list4 = list((1,2,3,4))
print(list1)
print(list2)
print(list3)
print(list4)

my_tuple = (1,2,3)
my_tuple = tuple((1, 2, 3))
print(my_tuple)

set1 = {"a","b","c"}
set2 = set(("a","b","c"))
print(set2)


empty_dict = {}
a =  {"one": 1, "two": 2 ,"three" : 3}
print(a["one"])

print(a.keys())
print(a.values())

a.update({"four" : 4})
print(a["four"])

# casting 
# integer | Float | String

x = int(1)
y = int(2.8)
z = int("3")

a = float(1)
b = float(2.3)
c = float("3.1")
d = float("1")

f = str(1)
g = str(1.12)
h = str("1teo")

try:
    d = float("! ")
    print(d)
except Exception:
    print("error")