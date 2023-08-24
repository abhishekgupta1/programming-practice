class myNewClass:
    pass

# class instantiation
my = myNewClass()


# constructor
class Animal :
    def __init__(self, voice):
        self.voice = voice
        
cat = Animal('Meow')
print(cat.voice)
    
dog = Animal("woof")
print(dog.voice)    


# call a method
class Dog:
     def bark(self):
         print("Ham-Ham")
Charlie = Dog()
Charlie.bark()     

class myClass:
    class_variable = "A class variable"

print(myClass.class_variable)

x = myClass()
 
# => A class variable!
print(x.class_variable)


# Super function
class ParentClass:
    def self_method(self):
        print("value")

class ChildClass(ParentClass):
    def self_method(self):
        return super().self_method()
    
# repr method
class Employee:
    def __init__(self,name):
        self.name = name
    
    def __repr__(self) -> str:
        return self.name

test = Employee("abhishek")
print(test)

#user defined exception
class CustomError(Exception):
    pass



class ParentClass:
    def print_self(self):
        print("A")

class ChildClass(ParentClass):
    def print_self(self):
        print("B")
        
print("---------------------")       
print(ParentClass().print_self())
print(ChildClass().print_self())



class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
class Dog(Animal):
    def sound(self):
        print("woof")

yoki = Dog("Yoki", 4)
print(yoki.name)
print(yoki.legs)
yoki.sound()



