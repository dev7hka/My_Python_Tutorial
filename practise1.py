from functools import reduce
import time
from bisect import bisect_left

def fact1(number):
    return 1 if (number == 1 or number == 0) else number * fact1(number - 1)


def fact2(number):
    f = 1
    for _ in range(2, number + 1):
        f *= _
    return f


# print(fact1(5))
# print(fact2(5))
# print((reduce((lambda x,y: x*y), [*range(1, 6)])))

def arms1(number):
    a = 0
    for _ in list(str(number)):
        a += int(_) ** 3
    return a == number


# print(arms1(153))
# print(153 == sum(map((lambda t: t**3), [int(z) for z in str(153)])))

def prime1(start, stop):
    primes = []
    for _ in range(start, stop + 1):
        if _ % 2 == 0 or _ % 3 == 0:
            continue
        isprime = True
        for __ in range(2, _ // 2 + 2, 2):
            if _ % __ == 0:
                isprime = False
                break
        if isprime:
            primes.append(_)
    return primes
# print(prime1(4, 17))

def fib1(number):

    if number <= 0:
        return 0
    if number < 2:
        return 1
    a = 0
    b = 1
    for i in range(2, number):
        c = a + b
        a = b
        b = c
    return b

def fib2(number):
    if number <= 1:
        return 0
    if number == 2:
        return 1
    return fib2(number-2)+fib2(number-1)

# print(fib1(9))
# print(fib2(9))

def sumnum(number):

    sm = 0
    for _ in range(1, number+1):
        sm += _ * _
    return sm
# print(sumnum(4))
# print(sum(map((lambda x: x**2), *[range(1, 4+1)])))

def rotate(arr, d):
    """
    rotate integer array 'arr'. Last 'd' element is removed and inserted to the head of the array
    :param arr: integer array
    :param d: step size(rotation amount)
    :return: int[]
    """
    tmp = []
    for _ in range(len(arr)-d, len(arr)):
        tmp.append(arr[_])
    arr = arr[0:len(arr)-d]
    i = 0
    for _ in tmp:
        arr.insert(i, _)
        i+=1
    return arr

def rotatereverse(arr, d):
    """
    rotate reversely integer array 'arr'. First 'd' element is removed and inserted to the end of the array
    :param arr: integer array
    :param d: step size(rotation amount)
    :return: int[]
    """
    tmp = []
    for _ in range(d):
        tmp.append(arr[_])
    arr = arr[d-1:]
    i = len(arr)
    arr.extend(tmp)
    return arr
arr = [1,2,3,4,5,6,7]
# print(rotate(arr,2))
start = time.time_ns()
(rotatereverse(arr,2))
stop = time.time_ns()
# print(stop-start)

def findremainder(arr, n):

    return reduce((lambda x,y: (x%n)*(y%n)%n), arr) % n

# print(findremainder({100, 10, 5, 25, 35, 14}, 11))

def ismonotonic(arr):

    mono = True if arr[0] <= arr[1] else False

    for _ in range(1, len(arr)-1):

        if (arr[_] >= arr[_+1], arr[_] <= arr[_+1])[mono] == False:
            return False
    return True

def ismonotonic2(arr):

    return (all(arr[i] <= arr[i+1] for i in range(1, len(arr)-1)) or
            all(arr[i] >= arr[i+1] for i in range(1, len(arr)-1)))

# print(ismonotonic([5,15,20,10]))
# print(ismonotonic2([25,24,20,20,10]))

def isInList(arr, n):

    arr.sort()
    i = bisect_left(arr, n)
    if i != len(arr) and arr[i] == n:
        return True
    return False
# print(isInList([1,2,3,3,4,5],-1))

def findduplicate(arr: list):

    dup = []
    di = dict()
    for _ in arr:

        if _ not in di.keys():
            di[_] = 1
        else:
            di[_]+=1

    for _, __ in di.items():
        if __ != 1:
            dup.append(_)
    return dup


# Python program to print
# duplicates from a list
# of integers
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
list2 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
list3 = [*range(2**14)]

start = time.time()
# print(findduplicate(list3))
stop = time.time()
# print("Mine", stop-start)

start = time.time()
# print(Repeat(list3))
stop = time.time()
# print("Other",stop-start)

def cumulativeSum(arr: list):
    """
    example-> input: [1,2,3,4,5,6] output: [1, 3, 6, 10, 15, 21]
    :param arr: integer list
    :return:  integer list
    """
    tmp = arr[0]
    cum = [arr[0]]
    for i in range(1, len(arr)):

        cum.append(arr[i]+tmp)
        tmp += arr[i]
    return cum
# print(cumulativeSum([10, 20, 30, 40, 50]))
# print([sum([10, 20, 30, 40, 50][0:x]) for x in range(0, len([10, 20, 30, 40, 50])+1)][1:])
x = [*range(1,10)]
y = 4
# print([x[i:i+y] for i in range(0, len(x),y)])

def sortListbyList(arr1: list, arr2: list):
    """
    example:
        list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
        Output : ['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']
    :param arr1: first list
    :param arr2: second list
    :return: sorted list
    """
    di = dict()
    li = []
    for _, __ in zip(arr1, arr2):
        if __ not in di.keys():
            di[__] = [_]
        else:
            di[__].append(_)
    for _ in sorted(di.keys()):
        li.extend(di[_])
    return li

def sortListbyListImproved(arr1: list, arr2: list):

    zipped = zip(arr2, arr1)
    li = [y for x, y in sorted(zipped)]
    return li

# print(sortListbyList(["a", "b", "c", "d", "e", "f", "g", "h", "i"], [ 0,   1,   1,    0,   1,   2,   2,   0,   1]))
# print(sortListbyListImproved(["a", "b", "c", "d", "e", "f", "g", "h", "i"], [ 0,   1,   1,    0,   1,   2,   2,   0,   1]))

def subStrings(string):
    pass

def listToDict(arr1: list, arr2: list):
    """
    input :  test_list = ["Gfg”, 3, "is”, 8], key_list = ["name”, "id”]
    Output :        [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]
    Explanation :   Values mapped by custom key, "name” -> "Gfg”, "id” -> 3
    :param arr1:
    :param arr2:
    :return:
    """
    li = []
    for _ in range(0,len(arr1)-1,2):

        di = {}
        a = arr1[_]
        b = arr1[_ + 1]
        di[arr2[0]] = a
        di[arr2[1]] = b
        li.append(di)
    return li

test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
key_list = ["name", "number"]
# print(listToDict(test_list, key_list))

def maxDistance(arr: list):

    li = dict()
    for _ in range(len(arr)):

        if arr[_] not in li.keys():
            li[arr[_]] = [_]
        else:
            li[arr[_]].append(_)
    key, idx = "", 0
    for _, __ in li.items():

        if __[len(__)-1] - __[0] > idx:
            idx = __[len(__)-1] - __[0]
            key = _
    return [key, idx]

# print(maxDistance([4, 5, 6, 4, 6, 3]))

def isPalindrome(string: str):

    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    else:
        return isPalindrome(string[1:-1])

x = "abcdxdcba"
# print(isPalindrome(x))
# print(x == x[::-1])

def checkVowels(string: str):

    string = set(string.lower())
    vowels = {"a","e","i","o","u"}
    return string.issuperset(vowels)

# print(checkVowels("geeksaiqweosdassu"))

def removeDuplicate(string: str):

    res = ""
    for _ in string:
        if _ not in res:
            res += _
    return res

# print(removeDuplicate("geeksforgeeks"))

















