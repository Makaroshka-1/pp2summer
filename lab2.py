#w3 lab from bool to for loop
#Booleans
def bool_ex1():
    print(10>9)
    #outputs True
def bool_ex2():
    print(10==9)
    #outputs False
def bool_ex3():
    print(10<9)
    #outputs False
def bool_ex4():
    print(bool("abc"))
    #outputs True
def bool_ex5():
    print(bool(0))
    #outpust False
#Operators
def operators_ex1():
    print(10 * 5)
def operators_ex2():
    print(10 / 2)
def operators_ex3():
    fruits = ["apple", "banana"] 
    if "apple" in fruits:
        print("Yes, apple is a fruit!")
def operators_ex4():
    if 5 != 10:
        print("5 and 10 is not equal")
def operators_ex5():
    if 5 == 10 or 4 == 4:
        print("At least one of the statements is true") 
#Lists
def lists_ex1():
    fruits = ["apple", "banana", "cherry"]
    print(fruits[1])
def lists_ex2():
    fruits = ["apple", "banana", "cherry"]
    fruits[0]="kiwi"
def lists_ex3():
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")     
def lists_ex4():
    fruits = ["apple", "banana", "cherry"]
    fruits.insert(1,"lemon")
def lists_ex5():
    fruits = ["apple", "banana", "cherry"]
    fruits.remove("banana")
def lists_ex6():
    fruits = ["apple", "banana", "cherry"]
    print(fruits[-1])
def lists_ex7():
    fruits = ["apple", "banana", "cherry"]
    print(fruits[2:5])
def lists_ex8(): 
    fruits = ["apple", "banana", "cherry"]
    print(len(fruits)) 
#Tuples
def tuples_ex1():
    fruits = ("apple", "banana", "cherry")
    print(fruits[0])    
def tuples_ex2():
    fruits = ("apple", "banana", "cherry")
    print(len(fruits))
def tuples_ex3():
    fruits = ("apple", "banana", "cherry")
    print(fruits[-1])
def tuples_ex4():
    fruits = ("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")
    print(fruits[2:5])

#Sets
def sets_ex1():
    fruits = {"apple", "banana", "cherry"}
    if "apple" in fruits:
        print("Yes, apple is a fruit!")
def sets_ex2():
    fruits = {"apple", "banana", "cherry"}
    fruits.add("orange")
def sets_ex3():
    fruits = {"apple", "banana", "cherry"}
    more_fruits=[""," ",""]
    fruits.update(more_fruits)
def sets_ex4():
    fruits = {"apple", "banana", "cherry"}
    fruits.remove("banana")
def sets_ex5():
    fruits = {"apple", "banana", "cherry"}
    fruits.discard("banana")
#Dictionaries
def dict_ex1():
    car ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(car.get("model"))
def dict_ex2():
    car ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    car["year"]=2020
def dict_ex3():
    car ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    car["color"]="red"
def dict_ex4():
    car ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    car.pop("model")
def dict_ex5():
    car ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    car.clear()
#If..else
def if_else_ex1():
    a = 50
    b = 10
    if a>b:
        print("Hello World")
def if_else_ex2():
    a = 50
    b = 10
    if a!=b:
        print("Hello World")
def if_else_ex3():
    a = 50
    b = 10
    if a==b:
        print("YES")
    else:
        print("NO")
def if_else_ex4():
    a = 50
    b = 10
    if a==b:
        print(1)
    elif a>b:
        print(2)
    else:
        print(3)
def if_else_ex5():
    if a == b and c == d:
        print("Hello")
def if_else_ex6():
    if a == b or c == d:
        print("Hello")
def if_else_ex7():
    if 5>2:
        print("YES")
def if_else_ex8():
    a = 2
    b = 5
    print("YES") if a==b else print("No") 
def if_else_ex9():      
    a = 2
    b = 50
    c = 2
    if a==c or b==c: 
        print("YES")
#While loop
def while_loop_ex1():
    i = 1
    while i < 6:
        print(i)
        i += 1
def while_loop_ex2():
    i = 1
    while i < 6:
        if i==3:
            break
        i+=1
def while_loop_ex3():
    i = 1
    while i < 6:
        if i==3:
            continue
        i+=1
def while_loop_ex4():
    i=1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")

#For loops
def for_loop_ex1():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
def for_loop_ex2():  
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            continue
        print(x)
def for_loop_ex3():
    for x in range(6):
        print(x)
def for_loop_ex4():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            break
    print(x)