#W3 Schools python tutorial 

#HOME

#INTRO

#GET STARTED
  
#SYNTAX

def syntax_ex1():
    print("Hello world!")

def syntax_ex2():
    if (5>2):
        print("YES")

#COMMENTS

def comments_ex1():
    #This is a comment
    print("Hello world!")

def comments_ex2():
    """
    This is 
    multiline
    comment
    """

#VARIABLES 

def variables_ex1():
    carname = "Volvo"

def variables_ex2():
    x = 50

def variables_ex3():
    x = 5
    y = 10
    print(x+y)

def variables_ex4():
    x = 5
    y = 10
    z = x + y
    print(z)

def variables_ex5():
    x,y,z = "Orange", "Banana", "Cherry"

def variables_ex6():
    x=y=z="Orange"

def variables_ex7(): 
    global x
    x = "fantastic"   

#DATA TYPES

def data_types_ex1():
    x = 5
    print(type(x))
    #the output will be: int

def data_types_ex2():
    x = "Hello World"
    print(type(x))
    #the output will be: str

def data_types_ex3():
    x = 20.5
    print(type(x))
    #the output will be: float

def data_types_ex4():
    x = ["apple", "banana", "cherry"]
    print(type(x))
    #the output will be: list

def data_types_ex5():
    x = ("apple", "banana", "cherry")
    print(type(x))     
    #the output will be: tuple
    
def data_types_ex6():
    x = {"name" : "John", "age" : 36}
    print(type(x))  
    #the output will be: dict

def data_types_ex7():
    x = True
    print(type(x))
    #the output will be: bool
   
#NUMBERS

def numbers_ex1():
    x = 5
    x=float(x)

def numbers_ex1():
    x = 5.5
    x = int(x)

def numbers_ex1():
    x = 5
    x = complex(x)

#CASTING

#STRINGS

def strings_ex1():
    x = "Hello World"
    print(len(x))

def strings_ex2():
    txt = "Hello World"
    x = txt[0]

def strings_ex3():
    txt = "Hello World"
    x = txt[2:5]

def strings_ex4():
    txt = "Hello World"
    x = txt.strip()

def strings_ex5():
    txt = "Hello World"
    txt = txt.upper()

def strings_ex6():
    txt = "Hello World"
    txt = txt.lower()

def strings_ex7():
    txt = "Hello World"
    txt.replace("H","J")

def strings_ex8():
    age = 36
    txt = "My name is John, and I am {}"
    print(txt.format(age))