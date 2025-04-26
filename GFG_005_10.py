#prblm_41: Anagram (GFG) 
    #Time Complexity: O(N + M)
def areAnagrams(s1, s2):
    hsp = {}
    for i in s1:
        if i not in hsp:
            hsp[i] = 1
        else:
            hsp[i] += 1
    for i in s2:
        if i not in hsp or hsp[i] == 0:
            return False
        else:
            hsp[i] -= 1
    for i in hsp:
        if hsp[i] > 0:
            return False
    return True

#prblm_42: Pallindrome String (GFG) 
    #Time Complexity: O(N)
def isPalindrome(s: str) -> bool:
    for i in range(len(s)):
        if i >= len(s)-i:
            break
        if s[i] != s[(len(s)-1)-i]:
            return False
    return True

#prblm_43: Check Equal Arrays (GFG) 
    #Time Complexity: O(N + M)
def checkEqual(self, a, b) -> bool:
    hsp = {}
    for i in a:
        if i not in hsp:
            hsp[i] = 1
        else:
            hsp[i] += 1
    for i in b:
        if i not in hsp:
            return False
        else:
            hsp[i] -= 1
    for i in hsp:
        if hsp[i] > 0:
            return False
    return True

#prblm_44: Reverse Words (GFG) 
    #Time Complexity: O(N)
def reverseWords(self, s):
    lst = s.split()
    lst = lst[::-1]
    st = ''
    for i in lst:
        st = st + ' ' + i
    return st.strip()

#prblm_45: Two Sum - Pair with Given Sum  (GFG & leetcode)                                 !!Important
    #Solution: 1                                               
    #Time Complexity: O(N²)    --> Linear Search (Time limit exceeds error)
def twoSum(self, arr, target):
    if len(arr) <= 1:
        return False
    for i in range(len(arr)-1):
        for j in range(1,len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False
    #Solution: 2                                Ref: CodeMeal                           
    #Time Complexity: O(N)    --> Hash Map
def twoSum(self, arr, target):
    hsp = {}
    for i in range(len(arr)):
        dif = target - arr[i]
        if arr[i] not in hsp:
            hsp[dif] = i
        else:
            return True
    return False

#prblm_46: Number of occurrence (GFG) 
    #Time Complexity: o(N)  --> Binary Search Approach
def countFreq(arr, target):
    count,pnt = 0,0
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            count += 1
            pnt = mid-1
            while pnt>=0 and arr[pnt] == target:
                count += 1
                pnt -= 1
            pnt = mid+1
            while pnt<len(arr) and arr[pnt] == target:
                count += 1
                pnt += 1
            return count
        elif arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            start = mid+1
    return count
arr = [1, 1, 2, 2, 2, 2, 3]
target = 4
#print(countFreq(arr,target))

#prblm_47: Bubble Sort (GFG) 
    #Time Complexity: o(N²)  --> Bubble Sort
def bubbleSort(self,arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

#prblm_48: First Repeating Element (GFG)                             !important 
    #Solution_1:
    #Time Complexity: O(N)  --> Time Exceeds Error
def firstRepeated(self,arr):
    hsp= {}
    for i in range(len(arr)):
        if arr[i] not in hsp:
            hsp[arr[i]] = 1
        else:
            hsp[arr[i]] += 1  
    for i in hsp:
        if hsp[i] > 1:
            return (arr.index(i))+1 
    return -1

    #Solution_2:                                    !!important_pattern
    #Time Complexity: O(N)
def firstRepeated(arr):
    seen = set()
    repeated = set()
    for val in arr:
        if val in seen:
            repeated.add(val)
        seen.add(val)
    for i in range(len(arr)):
        if arr[i] in repeated:
            return i + 1
    return -1

#prblm_49: Remove duplicates in Array (GFG) 
    #Time Complexity: O(N)
def removeDuplicates(arr):
    data = set()
    rp_arr = []
    for i in range(len(arr)):
        if arr[i] not in data:
            rp_arr.append(arr[i])
            data.add(arr[i])
        else:
            data.add(arr[i])
    return rp_arr
arr = [8, 7]
print(removeDuplicates(arr))

#prblm_50: Non Repeating Character (GFG) 
    #Time Complexity: O(N)
def nonRepeatingChar(self,s):
    hsp = {}
    for i in s:
        if i not in hsp:
            hsp[i] = 1
        else:
            hsp[i] += 1
    for i in hsp:
        if hsp[i] <= 1:
            return i
    return '$'