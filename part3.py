# from part2 import f3
# import part2
# import part2 as pt2
# from part2 import *
import time
"""
    - Everything is an object
    4 basics of OOP:
        - Encapsulation: bundling all the data of a class
        - Abstraction: hiding details
        - PolyMorphism: same interface for different types(Same method works different depending on implementation)
        - Inheritance: inherit methods and instances of parent class
    Higher Order Functions:
        - Take another function as argument
        - return another function
        - both
    - All Exceptions derive from BaseException
    - You can derive new Exceptions from Exception class
    - Some Exceptions: TypeError, ZeroDivisionError, IndexError, SyntaxError, StopIteration...   
    -   module: a .py file that contains classes and functions
        package: collection of modules
    - print(__name__): print the name of the module
    - __init__.py: used to mark directories as python package directories(simply makes the folder a package)    
    - 3 ways to import a module:
        -- import module_name
        -- from module_name import class_name
        -- from module_name import *
    - popular python libraries-packages: numpy, matplotlib, pandas, keras, tensorflow, scipy, pytorch, pygame, pillow, openCV, requests, NLK (Natural language toolkit)
                                        
"""
class Animal:

    def __init__(self, name, sound, move):
        self.name = name
        self.sound = sound
        self.move = move

    @classmethod
    def sound(cls, name, move):
        print(f"{name} is {move}")

    @staticmethod
    def move(name):
        print(name," is moving")

    def getName(self):
        print("My name is "+self.name)

cat = Animal("abcd", "meow","walking")
dog = Animal("xyz","hav","running")
# Animal.sound("abcd","running")
# Animal.move("abcd")
# cat.getName()
# dog.getName()
class Bird(Animal):

    eggcolor = "blue"  # can access from outside
    __furcolor = "green"  # Can't access from outside

    def __init__(self, name, sound, move, color):
        super().__init__(name, sound, move)
        self.color = color

    def getColor(self):
        print("My color is", self.color)

    def getName(self):
        print("I am "+self.name)
    def getEggColor(self):
        print(self.eggcolor)

bird = Bird("cicik", "cik","flying", "yellow")
# bird.getName()
# bird.getColor()
# Bird.sound("tip","hrring")
"""Higher Functions"""
def f1(func, number):  ## It is a higher order function
    print("It is f1")
    return func(number)
def f2(number):
    print("It is f2")
    return number
# print(f1(f2, 5))
"""Decorator"""
def ff(func):
    # print("It is ff from Decorator")
    def wrapit(number):
        print("It is wrapit")
        func(number)
    return wrapit
@ff
def fy(number):
    print("It is fy", number)
# fy(13)

def smart_divide(func):
    # print("I am going to divide")
    def smart(a,b):
        print("Let me check if dividable")
        if b == 0:
            return "It is not dividable, Sorry"
        return func(a,b)
    return smart
@smart_divide
def divideit(a,b):
    return a/b
# print(divideit(9,0))

def star(func):
    def starty(*args, **kwargs):
        print("*"*20)
        func(args, kwargs)
        print("*"*20)
    return starty
def hash(func):
    def hashy(*args):
        print("#"*20)
        func(args)
        print("#"*20)
    return hashy
# @star
@hash
def funcy(*args):
    for _ in args[0]:
        print(_ , "<->", end="")
    print()
# funcy(1,2,3,4,5)
def timer(func):
    def wrapper(*args):
        start = time.time()
        func(args)
        end = time.time()
        print(f"Function executed in {end-start}")
    return wrapper
@timer
def testFunc(*args):
    print(list(filter(lambda x: True if x%3312211 == 0 else False, [*range(2**25)])))
# testFunc()
"""Error Handling and Exceptions"""
def summy(numbers: list):

    try:
        print(sum(numbers))
        assert len(numbers) == 5
    except SyntaxError:  # Does not catch this error, don't know why
        print("Syntax Error")
    except TypeError as TE:
        print("There was a type Error:", TE)
    except ZeroDivisionError as ZDE:
        print("You CAN'T divide a number by zero:", ZDE)
    except:
        print("Don't know what but there is a problem")
    else:
        print("Okay, There was no problem buddy")
    finally:
        print("You are DONE")
# summy([1,2,3,4,5])
"""Generators"""
def giveFibonacci():
    """
    Fibonacci Function, however it is a generator function
    :return: int
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
        if a > 50:
            break
fib = giveFibonacci()
for _ in range(10):
    print(next(fib), end=" ")
print()
fib2 = giveFibonacci()
try:
    while True:
        print(next(fib2), end="-->")
except StopIteration:
    print("\nThat is enough of Fibonacci")
def doubleFib(nums):
    for num in nums:
        yield num ** 2
fib3 = doubleFib(giveFibonacci()) # That is called Composition
for _ in range(10):
    print(next(fib3), end=" ")
print()
# f3(5)
