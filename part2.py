from functools import reduce
"""
Data Types: List methods: append: add to end; clear: clear list; copy: new list with same item; count: #items; extend: add iterable to the end of list; index: index of first occurence
                          insert: insert to specified index; pop: remove last item(if index not given); remove: remove first occurence; reverse: reverse order; sort: sort the list
            Dictionary methods: clear: remove all; copy: copy dict; fromkeys: return a dict with given keys and value; items/keys/values: return key-value pair/keys/values; get: return value
                                pop: remove given key, return value; popitem: remove last inserted pair; setdefault: return value of key, if DNE, insert and return value; update: update w/ a dict
            Tuple methods: count: #element; index: index of first occurence;
            Set methods: add: add to set; clear: clear set; copy: copy set; difference: return difference of two set; difference_update: difference of two set is put to first one; discard: remove item
                         intersection: return intersection of two set; intersection_update: intersection of two set is put to first one; isdisjoint: return whether two set have intersection or not
                         issubset/issuperset: return whether set contains this set/vice versa; pop: remove random element; remove: same as discard, but gives error; union/update: union of two set/updated union
                         symmetric_difference: return symmetric differences of two set; symmetric_difference_update: updated symmetric_difference
            Operators: %, **, //, is, is not, in, not in, and, or, not, &, |, ^, ~, <<, >>
            *args and **kwargs: used when number of arguments of function is not known;

"""
"""List"""
li = [*range(5)]  # [0, 1, 2, 3, 4]
il = li[0:4:2]  # [0, 2]
illi = il + li  # [0, 2, 0, 1, 2, 3, 4]
il3 = il * 3  # [0, 2, 0, 2, 0, 2]
x = ["a"] * 3  # ['a', 'a', 'a']
ab = [x + y for x, y in zip([1, 3, 5], [2, 4, 6])]  # [3, 7, 11]
li[1:2] = [-1, -2, -3]  # [0, -1, -2, -3, 2, 3, 4]
del li[2:4]  # [0, -1, 2, 3, 4]
cd = ["p", "p", "p", "a", "b", "p", "p", "x"]
cd.remove("p")  # ['p', 'p', 'a', 'b', 'p', 'p', 'x']
ef = [x for x in cd if x != "p"]  # ['a', 'b', 'x']
"""Dictionary"""
di = {12: "abc", 24: "def"}
di2 = di.copy()
di2[36] = "xyz"  # {12: 'abc', 24: 'def', 36: 'xyz'}
key = {"a", "e", "i", "o", "u"}
val = [-1]
di3 = dict.fromkeys(key, (val))  # {'u': [-1], 'o': [-1], 'i': [-1], 'a': [-1], 'e': [-1]}
# print(36 in di2) # True
"""Tuple"""
# tu = tuple([1,2,3,1,4,5]); print(tu.index(1, 1)); print(tu.count(1)) #3 ; 2
"""Set"""
# se = {1,2,3,4,5,5};se.add(0);se2 = se.copy();se.discard(1);print(se2.difference(se));se.difference_update(se2)
# se = {1, 3, 10, 5};print(se.intersection(se2));se.intersection_update(se2);print(se.issubset(se2))
# se2.pop();se2.remove(1);print(se.symmetric_difference(se2));se.symmetric_difference_update(se2)
# print(se.union(se2));se.update(se2)
# print(set("abcd")) # {'a', 'b', 'd', 'c'}
# print(set(["abcd"])) # {'abcd'}
"""Ternary Operator"""
a = 3
b = 5
c = 7
# print(a) if a > b else print(b)         # 5
# print((a,b)[a>b])                       # 3
# print({True: b*3,False:a*2}[a<b])       # 15
# print((lambda: c, lambda: b)[c<b]())    # 7
min = c if c < b else b if b < a else a  # 3
"""lambda"""
# print((lambda x : x**2)(5)) # 25
# print(list(map((lambda a: a%7), [*range(5,50,6)]))) # [5, 4, 3, 2, 1, 0, 6, 5]
# print(reduce((lambda f, y: f*y), [2,3,4,5])) # 120
x = {"abc": 25, "def":23, "ghi":24}
# print(sorted(x.items(), key= lambda a: a[1]))
"""Interestings"""
# print(True == True) # True
# print(True is True) # True
# print("" == 1) # False
# print("" is 1) # SyntaxWarning
# print("a" == 1) # False
# print([] == 1) # False
# print([] == 0) # False
# print([] is 1) # SyntaxWarning
# print(10 == 10.0) # True
# print(10 is 10.0) # SyntaxWarning
# print([] == []) # True
# print([] is []) # False
# print(1 and 24) # 24
# print([x for x in "ABCD1234AXsadwqe1999ss.-x1" if x.isdigit()]) # ['1', '2', '3', '4', '1', '9', '9', '9', '1']
# print([1,2,3]*2) # [1, 2, 3, 1, 2, 3]
# print([1,2,3]*0) # []
# print([1,2,3,4,5][::-1]) # [5, 4, 3, 2, 1]
# print([x.replace("a","i").replace("c","t") for x in ["abcd","axef","ss","12"]]) # ['ibtd', 'ixef', 'ss', '12']
# print(", ".join(["abcd","axef","ss","12"]).replace("a","i").replace("c","t").split(", ")) # ['ibtd', 'ixef', 'ss', '12']
# print([(x,y) for x in range(5,8) for y in range(1,4)]) # [(5, 1), (5, 2), (5, 3), (6, 1), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3)]
def func1(num1):
    def func2(num2):
        return num1+num2
    return func2
add_10 = func1(10)
# print(add_10(55))
# print(print.__doc__) # docstring of print function
"""*args and **kwargs"""
def f1(*args):
    sm = 0
    for _ in args:
        sm+=_
    print(sm)
def f2(**kwargs):
    for _, __ in kwargs.items():
        print("{:<4}---> {}".format(_,__))
# f1(-5,-4,-3,-2,-1)
# f2(bir=1, iki=2, üç=3)
f3 = f1
del f1
# f3(-5,-4,-3,-2,-1)