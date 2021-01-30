"""
Python: - interpreted, high-level language
        - CPython: official interpreter (others: jython, pypy...)
        - data types: int, float, str, bool, list, tuple, dict, set, complex, None ('type' function: determine type of value or expression)
        - 'math' library: math functions and constants
        - single quote(') and double quote(") are same. triple double quote lets you write multiple line string
        - 'len': #items in an object, 'str'.count: number of char(s) in string, 'str'.find: first occurrence(index) of char(s) in string
        - Built-in Functions: abs: absolute value, all/any: return true/false if all/any items true, bin/hex: binary/hexadecimal version of a number, bool: boolean version of object,
          callable: returns true if object is callable, chr: return character from unicode, setattr/getattr/hasattr/delattr: operation on the property of an object,
          dir: return all properties/methods of an object, enumerate: return collection as an enumerate object, eval: evaluate given single string expression,
          exec: larger version of eval, filter: exclude items in an iterable object, int/float/oct: return integer/float/octal number, frozenset: make iterable object immutable(immutable set)
          hash: return hash value of (immutable)object, help: built-in help system, id: id of object, isinstance/issubclass: return true if object is an instance/subclass of given object
          iter: return an iterator object, map: return specified iterator with specified function applied to each item, max/min: return max/min in iterable, object: return empty object
          ord: return unicode of given character, repr: readable version of an object(calls __repr__ func.), reversed: return a reversed iterator, round: round number, slice: return a slice object
          sorted: sort iterable object, @staticmethod/@classmethod: convert method to static/class method, sum: sum the items of iterable, zip: return an iterator that aggregates from two or more iterable.
        - String Methods: capitalize: first character to upper case, casefold/lower: convert string into lower case, center: center align the string, count: #occurrence in a string, encode: encode version of string
          startswith/endswith: return true if string starts/ends with given value, find: search string, return index of first occur, otherwise -1, format: formats values in a string, index: similar to 'find'
          is(alpha/decimal/digit/identifier/numeric/lower/upper), isspace: true if all chr. are whitespaces, istitle: true if string is a title, join: join all items into one string, ljust/rjust:justified string
          lstrip/rstrip: remove leading/trailing characters, maketrans/translate: maketrans constructs transition table; translate translates using transition table, rfind/rindex: find last occurrence in string
          partition: search string, return a tuple ("before", "match","after"), rpartition: same with partition, but last occurence, replace: replace in string, split: split string by seperator, zfill: fill with zeros
          rsplit: same as split, but starts from right, and max can be specified, splitlines: split with "\n" (split line by line to a list), swapcase: lowercase to uppercase and vice versa, title: make string title.

"""

"""Concatenation"""
str1 = "abc"; str2 = "def"
str3 = str1+str2 # abcdef
str3 = "".join([str1, str2]) # abcdef
str3 = "%s% s"%(str1, str2) # abcdef
str3 = "{}{}".format(str1, str2) # abcdef
"""Slicing and Indexing"""
str1 = "abcdefgh"
str2 = str1[2:6] # cdef
str2 = str1[5:1:-1] # fedc
str2 = str1[::-1] # hgfedcba
str2 = str1.count("ab") # 1
str2 = str1.find("cd") # 2
str2 = f"It is a formatted {str1} string" #It is a formatted abcdefgh string
str2 = str1.replace("a","X") # Xbcdefgh
"""Built-in Functions"""
# print(all((1,2,3,"ab", False))) # False
# print(ascii("string ı is aç strin¾")) # 'string \u0131 is a\xe7 strin\xbe'
# print(bin(32)) # 0b100000
# print(bool(1>2)) # False
# print(callable(print)) # True
# print(chr(65)) # A
# print(complex("3+5j")) # (3+5j)
class xx:
    ab = 3
# print(getattr(xx, "ab")) # 3
setattr(xx, "ab", 5)
# print(getattr(xx, "ab")) # 5
delattr(xx, "ab")
# print(hasattr(xx, "ab")) # False
#print(dir(print))
# print(divmod(7,2)) # (3, 1)
# print(list(enumerate(str1))) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g'), (7, 'h')]
def even(number):
    if number%2:
        return False
    return True
test = filter(even, range(10))
# for _ in test:print(_,end=" ") # 0 2 4 6 8
# print(int("1")) # 1
# print("{0:.4f} {1:.3f} {2:b} {3:o} {4:x} {5:X} {6:e}".format(13.2451, 432.12, 43, 43, 43, 43, 39)) # 13.2451 432.120 101011 53 2b 2B 3.900000e+01
# print("{2} {0} {3} {3}".format("abc","def","hij","klm")) # hij abc klm klm
# print("{:<5}{:^10}{:>15}".format("abc","def","xyz")) # abc     def                xyz
# print("{:$^10}".format("lira")) # $$$lira$$$
# print("{0:+f},{1:+f},{0:-f},{1:-f},{0:f},{1:f},{0: f},{1: f}".format(2.71, -2.71)) # +2.710000,-2.710000,2.710000,-2.710000,2.710000,-2.710000, 2.710000,-2.710000
# print("{:,}  {:.2%}".format(1234567890, .8976)) # 1,234,567,890  89.76%
# print(list("abc")) # ['a', 'b', 'c']
# print(list(map(lambda x: x*x, range(2,8)))) # [4, 9, 16, 25, 36, 49]
def f(n): return n.upper()
# print(list(map(f, ["abc","def","xyz"]))) # ['ABC', 'DEF', 'XYZ']
# print(list(map(lambda n1, n2: n1**n2, [1,2,3,4,5],[2]*5))) # [1, 4, 9, 16, 25]
# print(list(map(list, ["abc","def"]))) # [['a', 'b', 'c'], ['d', 'e', 'f']]
# print(min({"abdcs":3, "defs":2,"xyz":1}, key=len)) # xyz
# print(pow(3,4)); print(pow(3,4,7)) # 81 ; 4
# a = "abcdefg"; b = slice(1,5,2); print(a[b]) # bd
# a = ["ab","cd","abc","defg","aa"]; print(sorted(a, key=len, reverse=True)) # ['defg', 'abc', 'ab', 'cd', 'aa']
# a = [1,2,3,4]; b = ("x","y","z"); c = {"+","$","#"}; d = zip(a,b,c); e = list(d); print(e); f,g,h = zip(*e); print(f,g,h) # [(1, 'x', '$'), (2, 'y', '+'), (3, 'z', '#')] \n (1, 2, 3) ('x', 'y', 'z') ('$', '+', '#')
# print("abcdef".endswith("ef", 1,6)) # True
# di = {"ab":"12", "cd":"34", "ef":"56"} ;print("__".join(di.values())) # 12__34__56
# print("lira".rjust(15,"$")) # $$$$$$$$$$$lira
# print("abcxxxe..,banana..,ab".lstrip("..,abcxe")) # nana..,ab
txt = "ABCD EFGH"
table1 = { 66 : 79, 68 : 80, 70 : None };table2 = txt.maketrans("BD","OP","F")
# print(txt.translate(table1));print(txt.translate(table2)) # AOCP EGH  \n AOCP EGH
# print("ABCDEFGH".partition("D")) #('ABC', 'D', 'EFGH')
# print("ABC_D_EF_F".rsplit("_",2)) # ['ABC_D', 'EF', 'F']
# print("abcdabcdbdbdaaaa".strip("a")) # bcdabcdbdbd
