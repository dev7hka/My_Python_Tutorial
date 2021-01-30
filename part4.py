import pathlib
import re
import pdb
import unittest
"""
    Two types of files: text and binary
    file opening modes: r: read only; w: write only; a: append; b: binary; t:text; rb: default mode; r+: both reading and writing; w+: both reading and writing;a+: both appending and reading
    Regular Expressions:
        - [abc]: a set of characters you wish to match (a or b or c) examples: [a-c]:a or b or c; [0-38]: 0 or 1 or 2 or 3 or 8; [^abc]: any character except a or b or c
        - 'a..c': any two character between a and c (like abbc) examples: 'a.*b': any match starting with a and ending with b;
        - ^ma*n$: start with m and end with n
        - +: one or more occurrences
        - ?: zero or one occurrences
        - ab{2,4}c: at least 2 b, at most 4 b (like abbbc) examples: [0-9]{3}-[0-9]{7}: a phone number like 555-3123121
        - a|b: alternation (or operator)(includes a or b or both)
        - (): group sub-patterns examples: (a|b|c)xz: abxz, axz, cabxzsa
    python re functions: findall: return a list of matches; split: split by regex; sub: like replace in strings; search: first occurrence is returned as match object
    debugging with pdb: p: print value e.g: p __file__; n (next, like stay local): execute until next line and stay in current function; s(step, like step into): execute current line and stop in different function(if there is)  
                        ll: long list, list content of all function; l: print 11 line around current line(also l .); c: continue till next breakpoint; b(reak): set breakpoints; unt: execute until line number is smaller than current(or given) one  
                        display/undisplay: to watch value(s) of variables; w: print stack trace;             
    Testing: 3 type of test result; 1- OK: passed the test, 2- FAIL: assertion error exception occured, 3- ERROR: an exception occured(other than AssertionError)
    
"""
"""File I/O"""
file1 = open("first.txt", mode="w", encoding="utf-8")
# print("is file1 writable:",file1.writable())
file1.write("This is calling from file1\n")
# print("no of file1:",file1.fileno())
# print("current position of file1 cursor:",file1.tell())
file1.seek(5)
file1.write("was")
# print("is file1 readable:",file1.readable())
# print(file1.close())
file1 = open("first.txt",mode="r", encoding="utf-8")
# print("read file1:",file1.read(), end="")
file1.close()
with open("second.txt","a+",encoding="utf-8") as file2: # no need to close
    file2.write("It is from file2, r u ready?\n")
    file2.seek(3,0) # second argument define starting point; 0 for beginning, 1 for current, 2 for end of file
    file2.write("was ") # didn't work
    file2.seek(0)
    # print("read file2:",file2.read(5))
    # print("read file2:",file2.readline(), end="")
    # print("file2 name:",file2.name)
    # print("is file2 closed:",file2.closed)
    # print("file2 mode:",file2.mode)
    # print("file2 encoding:",file2.encoding)
    # print("file2 errors:",file2.errors)
    # print("file2 newlines:",file2.newlines, end="")
    # print("file2 buffer:",file2.buffer)
"""pathlib module"""
# print(pathlib.Path.cwd())
# print(pathlib.Path.home())
# print(pathlib.Path("/it/is/a/directory"))
# print(pathlib.Path.home() / "It" / "is" / "also" / "a" / "directory")
# print(pathlib.Path.home().joinpath("It", "is", "also", "a", "directory"))
path = pathlib.Path.cwd() / "testing.txt"
path2 = pathlib.Path.cwd() / "2testing2.txt"
with open(path,"w") as file1:
    file1.write("It is testing 1\n")
with path2.open("w") as file2:
    file2.write("It is testing 2\n")
# print(path.read_text(), end="") # read as text
# print(path2.read_bytes(), end="") # read as binary
path.write_text("I am adding to testing 1\n")  # write as text
path2.write_bytes(b"I am adding to 2testing2\n") # write as binary
# print(path2.read_bytes())
# print(path2.read_text(), end="")
# print(path2.resolve()) # full directory
# print(path.parent) # parent directory
# print(path.parent == pathlib.Path.cwd()) # they are same because path is created as full directory
path3 = pathlib.Path("abc.txt")
# print(path3.parent) # Attention !!!
# print(path3.parent == pathlib.Path.cwd()) # they are not same because path3 is represented as .
# print("name:",path2.name)
# print("stem:",path2.stem)
# print("anchor:",path2.anchor)
# print("drive:",path2.drive)
# print("parts:",path2.parts)
# print("root:",path2.root)
# print("suffix:",path2.suffix)
# print("as_uri:",path2.as_uri())
# print("as_posix:",path2.as_posix())
# print("as_posix:",list(path2.parents))
# print(list(pathlib.Path.cwd().glob("*.py")))
path4 = pathlib.Path.cwd() / "file io files"
if path4.exists():
    # print("'File io files' is created")
    pass
path2.replace(path4)
"""Regular Expressions"""
pattern = 'ac..ve{1}'
string = "it is an acvivee program for activeveness and acsivedd"
# print(re.findall(pattern, string))
# print(re.findall('a.', string))
# print(re.split("ve", string))
# print((re.search("v", string)))
# print(re.search('[ab]', "it is not truae"))
# print(re.search('[a-f,1-47]', "it is no7t tru"))
# print(re.search('[a-f,1-47]', "it is no7t tru"))
# print(re.search('..', "it is not trnou").span())
# print(re.search('..', "it is not trnou").string)
# print(re.search('..', "it is not trnou").re)
# print(re.search('..', "it is not trnou").group())
# print(re.match('^i', "it is not trnou"))
# print(re.search('^i.*u$', "it is not trnou"))
# print(re.findall('is*s', "it is a good issf iss that doissz doiss"))
# print(re.split('is*s', "it is a good issf iss that doissz doiss"))
# print(re.sub('is*s', "doo", "it is a good issf iss that doissz doiss"))
# print(re.search('is*s', "it is a good issf iss that doissz doiss"))
"""Debugging"""
# breakpoint()
# print("x")
def f1():
    print("it is f1")
    def f2():
        print("it is f2")
        for _ in range(10):
            print(_, end="-")
        def f3():
            print("it is f3")
        f3()
    f2()
# f1()
# print("it is main")
"""Testing"""
def isitokay(a, b):
    c = a > b
    return c
def funcy(vava):

    raise TypeError if type(vava) != int else None

class Tester(unittest.TestCase):

    def test_1(self):     # every test starting with test_ will run automatically
                          # No need to call these test functions. Python will test if they start with test_

        val1 = 5; val2="0"; expected = False
        # result = isitokay(val1, val2)
        # self.assertEqual(result, expected)
        self.assertRaises(TypeError, funcy, val2)
    def test_2(self):

        val1 = [1,2,3]; val2 = 4; expected = False
        result = isitokay(val1, val2)
        self.assertEqual(result, expected)
        self.assertTrue(not result)
        self.assertFalse(result)

print(re.findall("[0-9]{3}-[0-9]{7}", "531-0314929111-2131232"))