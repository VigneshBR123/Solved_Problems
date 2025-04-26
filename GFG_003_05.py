#prblm_21: Kth from End of Linked List (GFG)            !Important
    #Time Complexity: O(N)
def getKthFromLast(self, head, k):
    cur = head
    length = 1
    while cur.next != None:
        length += 1
        cur = cur.next
    if k > length:
        return -1
    else:
        pos = (length - k)
        cur = head
        while pos != 0:
            cur = cur.next
            pos -= 1
        return cur.data
    
#prblm_22: Remove Duplicates from a Sorted Linked List (GFG)            
    #Time Complexity: O(N)
def removeDuplicates(head):
    cur = head
    while cur.next != None:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next

#prblm_23: Reverse a linked list (GFG)            !Important
    #Time Complexity: O(N)
def reverseList(self, head):
    cur = head
    pre = None
    while cur != None:
        nxt = cur.next
        cur.ref = pre
        pre = cur
        cur = nxt
    while pre != None:
        print(pre.data, end=" ")
        pre = pre.ref
#prblm_24: Print Linked List (GFG)          
    #Time Complexity: O(N)
def printList(self, head):
    cur = head
    while cur != None:
        print(cur.data, end=" ")
        cur = cur.next

#prblm_25: Delete in a Singly Linked List (GFG)         
    #Time Complexity: O(N)
def deleteNode(head, x):
    cur = head
    count = 1
    while cur != None:
        if x == 1:
            head = cur.next
            break
        elif count+1 == x:
            cur.next = cur.next.next
            break
        count += 1
        cur = cur.next
    cur = head
    while cur != None:
        print(cur.data, end=" ")
        cur = cur.next