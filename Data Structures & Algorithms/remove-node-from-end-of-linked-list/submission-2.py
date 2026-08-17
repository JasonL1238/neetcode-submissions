# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        first = head
        while not first == None:
            first = first.next
            length += 1
        
        i = head
        prev = None
        nex = i.next
        N = length - n

        print(N)
        while N > 0:
            prev = i
            i = nex
            nex = i.next  
            N -= 1

        if prev == None and nex == None:
            return None
        elif prev == None and not nex == None:
            return nex
        
        prev.next = nex
        return head
            

