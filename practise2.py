import math

from typing import List


def duplicateZeros(arr: list) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    """
    Input:  [1,0,2,3,0,4,5,0]
    result: [1,0,0,2,3,0,0,4]
    Output: null
    """
    """
    _ = 0
    while _ < len(arr):
        if arr[_] == 0:
            for __ in range(len(arr)-1, _, -1):
                arr[__] = arr[__ - 1]
            _ += 1
        _+=1
    print(arr)
    """
# duplicateZeros([1,0,2,3,0,4,5,0])
def stickCheck(arr:list, H):

    li = [x-H for x in arr if x >= H]
    li = [x for x in li if x != 0]
    tmp = len(set(li))
    if tmp != 1 and tmp != 0:
        return False
    return True

def stickProblem(arr: list):
    mylist = arr.copy()
    count = 0
    arr.sort()
    while len(mylist) > 0:
        print(mylist)
        H = mylist[len(mylist)-1]
        while stickCheck(mylist, H) == True and H > -1:
            H-=1
        H+=1
        for _ in range(len(mylist)):
            if mylist[_] > H:
                mylist[_] = H
        count+=1
        if len(set(mylist)) == 1 and H != mylist[0]:
            break
    print(count)

# stickProblem([1,2,3])
# your code goes here

"""
Input:
2
100 1 1 2 2
100 34 34 5 3

Output:
Case #1: 100
Case #2: 86
"""
def later():

    T = int(input())
    for i in range(T):
        res = input().split(" ")
        N, S1, V1, S2, V2 = int(res[0]), int(res[1]), int(res[2]), int(res[3]), int(res[4])
        """
        x = S1*a + S2*b
        y = V1*a + V2*b
        """
        best = [0, 0, 0]  # [val, x, y]
        for i in range(N//S1,0,-1):
            if i*S1 > N:
                break
            for j in range((N - i)//S2, 0,-1):
                tmpSize = S1*i + S2*j
                tmpVal = V1*i + V2*j
                if tmpVal > best[0] and tmpSize <= N and tmpSize > 0:
                    best = [tmpVal, i, j]
                if tmpSize < 0:
                    break
                if tmpVal < best[0]:
                    break
        print(best[0])

# later()
def isprime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for _ in range(3,number//2+1, 2):
        if number % _ == 0:
            return False
    return True

def primesBetweenTwo(num1, num2):
    x = num1
    if num1 % 2 == 0:
        x = num1+1
    for _ in range(x, num2+1, 2):
        if isprime(_):
            print(_)

def mainy():

    T = int(input())
    for i in range(T):
        res = input().split(" ")
        num1, num2 = int(res[0]), int(res[1])
        primesBetweenTwo(num1, num2)
# mainy()

"""
3 3 1 2
.x.
x.x
.x.
--------
..xx..
xx..xx
..xx..
"""

def weirdo():

    res = input().split(" ")
    row, col = int(res[0]), int(res[1])
    zr, zc = int(res[2]), int(res[3])

    matrix = []
    for _ in range(row):
        string = ""
        line = input()
        for __ in line:
            string += __ * zc
        string+="\n"
        string *= zr
        matrix.append(string)
    for _ in matrix:
        print(_, end="")

# weirdo()

def binary(arr: list, target: int):

    if len(arr) == 0:
        return -1
    lo = 0
    hi = len(arr)
    while lo <= hi:
        mid = int(lo + (hi-lo)/2)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid+1
        else:
            hi = mid -1

    return -1

def mm(arr: list, target: int):

    lefty = binary(arr, target)

    if lefty == -1:
        return [-1,-1]
    i = lefty
    while arr[i] == target:
        i+=1
    return [lefty,i-1]

# print(mm([5,7,7,8,8,10], 8))

def swap(li: list, count: int, track):

    if count == 0 and li[0] == 1:
        track[0]+=1
        return
    elif count == 0 and li[1] == 1:
        track[1]+=1
        return
    elif count == 0 and li[2] == 1:
        track[2]+=1
        return
    if li[1] == 1:
        li[0], li[1] = li[1], li[0]
        swap(li, count - 1, track)
        li[0], li[2] = li[2], li[0]
        swap(li, count - 1, track)
    elif li[0] == 1:
        li[0], li[1] = li[1], li[0]
        swap(li, count - 1, track)
    elif li[2] == 1:
        li[0], li[2] = li[2], li[0]
        swap(li, count - 1, track)
    return track
def findTheRing():
    T = int(input())
    for _ in range(T):
        line = input().split()
        index = int(line[0])
        N = int(line[1])
        li = [0, 0]
        li.insert(index, 1)
        if N == 0:
            print(index)
        elif index == 1:
            print("1") if N % 2 == 0 else print("0")
        else:
            print((N%2))


# code

def wordCheck(word1: str, word2: str):
    """
    check if word1 can be found in word2
    e.g:
    word1 = "apple", word2 = "abpcplea"
    word1 is in word2
    """
    x = len(word1)
    y = len(word2)
    word1index = 0
    word2index = 0
    while word1index < x and word2index < y:

        if word1[word1index] == word2[word2index]:
            word1index += 1
            word2index += 1
        else:
            word2index += 1

    if x == word1index:
        return True
    return False

def largestWordinDict():

    T = int(input())
    for _ in range(T):

        di = []
        total = int(input())
        line = input().split()

        for __ in line:
            di.append(__)

        string = input()
        maximum = ""
        for i in di:

            if wordCheck(i, string) and len(i) > len(maximum):
                maximum = i
        print(maximum)

# largestWordinDict()


class Solution:

    def binarySearch(arr: list, target: int) -> int:

        if len(arr) == 0:
            return -1
        lo = 0
        hi = len(arr)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                lo = mid + 1
            elif arr[mid] > target:
                hi = mid - 1
        return -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        li = sorted(nums)
        print(Solution.binarySearch(li, target-104))
        for i in range(len(li)):
            y = Solution.binarySearch(li, target - li[i])
            if y != -1 and y != i:
                num1 = nums.index(li[i])
                num2 = nums.index(li[y])
                if num1 == num2:
                    num2 = nums.index(li[i], num1+1)
                if num1 == num2:
                    num2 = nums.index(li[i],0, num1)
                return [num1, num2] if num1 <= num2 else [num2, num1]

        return [-1,-1]

sol = Solution()
z = [591,955,829,805,312,83,764,841,12,744,104,773,627,306,731,539,349,811,662,341,465,300,491,423,569,405,508,802,500,747,689,506,129,325,918,606,918,370,623,905,321,670,879,607,140,543,997,530,356,446,444,184,787,199,614,685,778,929,819,612,737,344,471,645,726]
print(sol.twoSum(z, 789))
print(z[10], z[55])