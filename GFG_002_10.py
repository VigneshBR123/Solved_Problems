#prblm_11: Print 1 to N without loop (GFG)          !Important
    #Time Complexity: O(N)
def printNos(n):
    if n == 0:  
        return
    print(n-1)
    printNos(n - 1)
    print(n, end=" ")
n = 3
#printNos(n)

#prblm_12: Rotate Array by 1 (GFG)
    #Time Complexity: O(N)
def rotate(arr):
    arr.insert(0,arr[len(arr)-1])
    arr.pop()
    return arr
ary = [1,2,3,4,5]
#print(rotate(ary))         O/P: [5,1,2,3,4]

#prblm_13: Value Equal To Index Value (GFG)
    #Time Complexity: O(N)
def valueEqualToIndex(arr):
    lst = []
    for i in range(len(arr)):
        if i+1 == arr[i]:
            lst.append(i+1)
    return lst

#prblm_14: LCM And GCD (GFG)                        !Important
    #Solution: 1 --> Normal Approach
def lcmAndGcd(a : int, b : int):
    def lcm(a,b):                   #--> LCM
        lcm = 1
        x = 2
        while a != 1 or b != 1:
            if a%x == 0 and b%x == 0:
                a /= x
                b /= x
                lcm *= x
            else:
                if a%x == 0:
                    a /= x
                    lcm *= x
                if b%x == 0:
                    b /= x
                    lcm *= x
            if a%x != 0 and b%x != 0:
                x += 1
        return lcm
    def gcd(a,b):                   #--> GCD
        gcd = 1
        x = 2
        while a != 1 or b != 1:
            if a%x == 0 and b%x == 0:
                a /= x
                b /= x
                gcd *= x
            else:
                if a%x == 0:
                    a /= x
                if b%x == 0:
                    b /= x
            if a%x != 0 and b%x != 0:
                x += 1
        return gcd
    lst = [lcm(a,b),gcd(a,b)]
    return lst
    #Time Complexity: O(min(a,b))      --> Run Time: 0.12Sec
    #Space Complexity:O(1)
#print(lcmAndGcd(18,25))
    #Solution_2: Optimized Solution    --> Ecuclidean Algorithm
def LCM_and_Gcd(a,b):
    def gcd(a,b):
        while b!=0:
            temp = a
            a = b
            b = temp%b
        return a
    gcd = gcd(a,b)
    def lcm(a,b,gcd):
        lcm = (a*b)//gcd
        return lcm
    lcm = lcm(a,b,gcd)
    return [lcm,gcd]
    #Time Complexity: O(log(min(a,b)))      --> Run Time: 0.05Sec
    #Space Complexity:O(1)
#print(LCM_and_Gcd(5,10))

#prblm_15: Alternates In Array (GFG)
    #Time Complexity: O(N)
def getAlternates( arr):
    return arr[::2]

#prblm_16: First Occurance (GFG)
    #Time Complexity: O(N*M)
def firstOccurence(txt,pat):
    if pat in txt:
        return txt.index(pat)
    else:   
        return -1
#print(firstOccurence('GeeksForGeeks','For'))

#prblm_17: Count Linked List Nodes (GFG)                !Important
    #Time Complexity: O(N)
    #Space Complexity: O(1)
def getCount(head):
    count = 0
    cur = head
    while cur != None:
        count += 1
        cur = cur.next
    return count 

#prblm_18: Linked List Insertion at End (GFG)            !Important
    #Time Complexity: O(N)
    #Space Complexity: O(1)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertAtEnd(self,head,x):
    newNode = Node(x)
    if head == None:
        head = newNode
    else:
        cur = head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
        
    cur = head
    while cur != None:
        print(cur.data, end=" ")
        cur = cur.next

#prblm_19: Insert in Middle of Linked List (GFG)            !Important
    #Time Complexity: O(N)
def insertInMiddle(self, head, x):
    cur = head
    tot = 0
    while cur != None:
        tot += 1
        cur = cur.next
    
    newNode = Node(x)
    if tot == 0:
        head = newNode
    elif tot == 1:
        head.next = newNode
    else:
        tot = round((tot / 2)+0.1)          # round(1.5) = 2 but round(2.5) = 2 --> Closet even didgit
        cur = head                          # to fix we add 0.1 and make round it.
        count = 0
        while count != tot-1:
            count += 1
            cur = cur.next
        newNode.next = cur.next
        cur.next = newNode
        
    cur = head
    while cur != None:
        print(cur.data, end=' ')
        cur = cur.next

#prblm_20: Middle of Linked List (GFG)            !Important
    #Time Complexity: O(N)
def getMiddle(self, head):
    cur = head
    tot = 0
    while cur != None:
        tot += 1
        cur = cur.next
    if tot == 0:
        print(' ')
    else:                                       #different logic from 19th prblm
        cur = head
        tot_1 = round((tot/2)+0.1)
        count = 0
        if tot%2 != 0:
            while count != tot_1-1:
                count += 1
                cur = cur.next
        else:
            while count != tot_1:
                count += 1
                cur = cur.next
        return cur.data