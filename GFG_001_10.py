import math                 #For prblm_9

#prblm_1: Peak Element (GFG)
    #Time Complexity: O(N) --> Linear Search || We can optimize it using 'Binary Search'
def peakElement(arr):
    for i in range(len(arr)):
        if i == 0 and arr[i] > arr[i+1]:
            return True
        elif i == len(arr)-1 and arr[i] > arr[i-1]:
            return True
        else:
            if (arr[i] > arr[i-1]) and (arr[i] > arr[i+1]):
                return True
    return False
arr = [1, 2, 4, 5, 7, 8, 3]
#print(peakElement(arr))
    #Optimized Solution --> Bineary Search  Time Complexity: O(logN)
def peakElement_2(arr):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end)//2
        pass #Didn't get better idea about logic.
    return -1
#print(peakElement_2(arr))

#prblm_2: Largest Element In Array (GFG)
    #Time Complexity: O(N)
def largest(arr):
    return max(arr)                 # I used here built-in, there is many alternative approaches.
#print(largest(arr))

#prblm_3: Sum of Natural Numbers (GFG)
    #Time Complexity: O(1)
def seriesSum(n : int) -> int:
    return round((n/2)*(n+1))       # Simple Mathematics Approach
n = 5
#print(seriesSum(n))

#prblm_4: Array Search (GFG)
    #Time Complexity: O(log N) --> Binary Search
def search(arr, x):
    arr_1 = sorted(arr)
    start,end = 0,len(arr_1)-1
    while start <= end:
        mid = (start+end)//2
        if arr_1[mid] == x:
            return arr.index(arr_1[mid])
        elif arr_1[mid] < x:
            start = mid+1
        elif arr_1[mid] > x:
            end = mid-1
    return -1
ary = [1, 2, 3, 4]
x = 3
#print(search(ary,x))

#prblm_5: Array Subset (GFG)  --> *Important
    #Solution: 1
def isSubset(a, b):
    for i in b:                 
        if i not in a:          
            return False
        a.remove(i)             
    return True
    #Time Complexity: O(N²) --> Error: Time Limit exeeds
    #Solution: 2                        a.sort() --> Time Complexity: O(N logN)
def isSubset(a, b):
    for i in range(len(b)):     #O(N)
        if b[i] not in a:       #O(M)
            return False
        a[a.index(b[i])] = -1   #O(M)
    return True
    #Time Complexity: O(N x M) --> Error: Time Limit exeeds
    #Solution: 3                        
def isSubset(a, b):
    freq = {}
    for i in a:                 #O(N)
        freq[i] = freq.get(i, 0) + 1
    for i in b:                 #(M)
        if i not in freq or freq[i] == 0:       #if i not in freq --> O(1)                                      
            return False                        #because dict in Python uses hash table under the hood.
        freq[i] -= 1
    return True
    #Time Complexity: O(N + M) --> Efficient Solution

#prblm_6: Largest Element In Array (GFG)
    #Time Complexity: O(N)
def reverseString(s: str) -> str:
    return s[::-1]  
s = 'Greeks'
#print(reverseString(s))

#prblm_7: Largest Element In Array (GFG)
    #Time Complexity: O(logN)   ---> Binary Search
def searchInSorted(arr, k):
    start,end = 0,len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == k:
            return True
        elif arr[mid] > k:
            end = mid-1
        elif arr[mid] < k:
            start = mid+1
    return False
arr = [1,2,3,4]
k = 3
#print(searchInSorted(arr,k))

#prblm_8: Reverse Array Groups (GFG)
    #Time Complexity: O(N)
def reverseInGroups(arr, k):
    if len(arr) <= k:
        return arr[::-1]
    else:
        i = 0
        grp_len = k
        while i < len(arr):
            print(i,grp_len)
            arr[i:grp_len] = arr[i:grp_len][::-1]       #here I learned - how reverse only a part of array
            if (len(arr) - k) <= k:
                grp_len += len(arr)
            else:
                grp_len += k    
            i += k
        return arr
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 2
#print(reverseInGroups(lst,k))

#prblm_9: Reverse Array Groups (GFG)
    #Time Complexity: O(√n)
def isPrime(n):
    if n == 1:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True
n = 7
#print(isPrime(n))

#prblm_10: Reverse Array Groups (GFG)   --> With out using built-in
    #Time Complexity: O(N)
def get_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        elif arr[i] > max_val:
            max_val = arr[i]
    return min_val, max_val
lst = [3, 2, 1, 56, 10000, 167]
print(get_min_max(lst))