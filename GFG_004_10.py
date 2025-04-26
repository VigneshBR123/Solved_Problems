#prblm_31: Missing In Array (GFG)            !Important
    #Time Complexity: O(N)
def missingNumber(arr):
    a = len(arr)+1
    if (a%2) == 0:
        a = (a*(a/2))+(a/2)
    else:
        a = (a*round((a/2)-0.1))+a
    for i in arr:
        a -= i
    return round(a)
    # Simple Version of Code
    total = a * (a + 1) // 2            #Elementory Formula
    return total - sum(arr)
arr = [1,2,4,5]
#print(missingNumber(arr))

#prblm_32: Second Largest (GFG)            !Important
    #Time Complexity: O(N logN)                   arr.sort() --> Time Complexity: O(N logN)
def getSecondLargest(arr):
    arr.sort()              #O(N logN)
    high = arr[len(arr)-1]
    i = 2
    while i<len(arr) and high == arr[len(arr)-i]:   #O(N)
        i += 1
    if arr[len(arr)-i] == high:
        return -1
    else:
        return arr[len(arr)-i]
arr = [1,2,4,5]
#print(getSecondLargest(arr))

#prblm_33: Array Leaders (GFG)            !Important
    #Time Complexity: O(N)
def leaders(arr):
    lst = []
    high = 0
    i = 1
    while (len(arr)-i) >= 0:
        j = len(arr)-i
        if arr[j] >= high:
            high = arr[j]
            lst.append(high)
        i += 1
    return lst[::-1]
lst = [16, 17, 4, 3, 5, 2]
#print(leaders(lst))

#prblm_34: Array Duplicates (GFG) 
    #solution: 1
def findDuplicates(arr):
    arr.sort()
    lst = []
    j = ''
    for i in range(len(arr)):
        if j != arr[i]:
            if i<len(arr)-1 and arr[i] == arr[i+1]:
                lst.append(arr[i])
                j = arr[i]
    return lst
    #Time Complexity: O(N logN) --> Time taken: 1.31 seconds 
    #solution: 2                --> More efficient
def findDuplicates_2(arr):
    freq = {}
    lst = []
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1        # Space complexity: O(K)
    for i in freq:
        if freq[i] >= 2:
            lst.append(i)
    return lst
    #Time Complexity: O(N+M)      --> Time taken: 0.71 seconds
lst = [1, 8, 4, 3, 6, 9, 5, 7, 2, 7, 0]
#print(findDuplicates_2(lst))    

#prblm_35: Equilibrium Point (GFG)            !!Important
def findEquilibrium(arr):
    left = 0
    right = sum(arr)
    for i in range(len(arr)):
        right -= arr[i]
        if left == right:
            return i
        left += arr[i]
    return -1
    #Time Complexity: O(N)
    """
    left = 0
    right = 0
    for i in range(len(arr)):
        left = sum(arr[0:i])
        right = sum(arr[i+1:len(arr)])
        if left == right:
            return i+1
    return -1
    """
    #Approach connect but,
    #Time Complexity: O(N²)    --> Time limit exceeds
    """
    flag = 0
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if sum(arr[:mid]) == sum(arr[mid+1:len(arr)]):
            return mid
        elif (sum(arr[:mid]) > sum(arr[mid+1:len(arr)])):
            if flag == 2:
                return -1
            else:
                end = mid-1
                flag = 1
        elif (sum(arr[:mid]) < sum(arr[mid+1:len(arr)])):
            if flag == 1:
                return -1
            else:
                start = mid+1
                flag = 2
    return -1
    """
    #Wrong Approach 
lst = [-7, 1, 5, 2, -4, 3, 0]
#print(findEquilibrium(lst))

#prblm_36: Array Search (GFG)     --> Binary Search            !Important
    #Time Complexity: O(logN)
def binarysearch(arr, k):
    in_fnd = -1
    start = 0 
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == k:
            in_fnd = mid
            end = mid-1         #notable
        elif arr[mid] > k:
            end = mid-1
        else:
            start = mid+1
    return in_fnd
arr = [1,1,1,4]
k = 4
#print(binarysearch(arr,k))

#prblm_37: Two sum -Pairs with 0 Sum (GFG)            !Important
    #Time Complexity: O(N logN)
def getPairs(self, arr):
    tot = {}
    lst = []
    for i in arr: #O(n)
        if i in tot:
            tot[i] += 1
        else:
            tot[i] = 1
    for i in tot: #O(n)
        if i == 0:
            if tot[i] > 1:
                lst.append([i,i])
        elif i < 0 and abs(i) in tot:
            lst.append([i,abs(i)])
    lst.sort() #O(n logn)
    return lst
arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
#print(getPairs(arr))

#prblm_38: Count Digits (GFG)
    #Time Complexity: O(N)
def evenlyDivides(self, n):
    x = str(n)
    count = 0
    for i in x:
        if int(i) != 0:
            if n % int(i) == 0:
                count += 1
    return count

#prblm_38: Floor in a Sorted Array  (GFG)                                               !!Important
    #Solution: 1                                               
    #Time Complexity: O(N²)    --> Time limit exceeds     --> Used Binary Search Why ?
def findFloor(self, arr, x):
    fn_idx = -1
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == x:
            if mid < len(arr)-1 and arr[mid+1] == x:        # Goes with --> Linear Search*
                start = mid+1
            else:
                return mid
        elif arr[mid] < x:
            fn_idx = mid
            start = mid+1
        else:
            end = mid-1
    return fn_idx
    # Solution: 2
    #Time Complexity: O(logN)    --> Binary Search
def findFloor(self, arr, x):
    fn_idx = -1
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == x:
            fn_idx = mid
            start = mid + 1
        elif arr[mid] < x:
            fn_idx = mid
            start = mid+1
        else:
            end = mid-1
    return fn_idx

#prblm_39: Union of Arrays with Duplicates          (GFG) 
    #Time Complexity: O(N + M)
def findUnion(self, a, b):
    hap = {}
    for i in a:
        if i not in hap:
            hap[i] = 1
        else:
            hap[i] += 1
    for i in b:
        if i not in hap:                           #Short Version    -->    Time Complexity: O(N + M)
            hap[i] = 1                             #    return len(set(a) | set(b))
        else:                                      #    '|'     --> Union Operator
            hap[i] += 1
    return len(hap)

#prblm_40: Power Of 2 (GFG) 
    #Time Complexity: O(logN)
def isPowerofTwo(n):
    if n == 0:
        return False
    while n > 0:                                #   Efficient Solution:                     !!important
        if n%2 != 0 and (n//2)>0:               #   Computer Trick --> Time Complexity: O(1)
            return False                        #   return n > 0 and (n & (n - 1)) == 0
        else:
            n = n//2
    return True
#print(isPowerofTwo(5))

