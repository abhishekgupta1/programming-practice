f = open("E:\GitProjects\programming-practice\Python\QuickRef_Python\welcome.txt", "r")
print(f.read())


with open("E:\GitProjects\programming-practice\Python\QuickRef_Python\welcome.txt", "r", encoding='utf8') as file:
    for line in file:
        print(line)