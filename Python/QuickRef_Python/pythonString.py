hello = "helloworld"
print(hello[1])
print(hello[-1])

for char in "char":
 print(char)
   
#  01234567
#  my bacon
# -7654321

bacon = "my bacon"
print(bacon[-8])

s = '123 ' * 5
print(s+" ")

s = "12345" * 5
print(s[2::5])
print(s[::5])
print(s[::-5])
print(s[::-1])


stringLength = "helloabhishek"
print(len(stringLength))
print ("abhishek" in stringLength)

name = "abhishek"
Surname = "gupta"
age = 10
print("Hello, %s!" % name)
print("%s is %s years old."   % (name,Surname))

print("%s is %s years old" %(name,Surname))
print("%d value"%age)


# format method
txt1 = "my name is {fname}, i am at {age}".format(fname="jhon", age = 20 )
txt2 = "my name is {0}, i am {1}".format("abhishek", 1)
txt3 = "my name is {}, i am {}".format("abhishek", 2)
print(txt1,txt2,txt3)

print("abhishe".join([" 1 "," 2 "]))

print("helloworld".endswith("world"))
print("helloworld".startswith("hello"))


