# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head.next == None:
            return

        behind = None
        first = head
        second = head
        while True:
            if second == None or second.next == None:
                break
            behind = first
            first = first.next
            second = second.next.next
        
        behind.next = None

        prev = None

        while not first == None:
            temp = first.next
            first.next = prev
            prev = first
            first = temp

        front = head

        while not prev == None:
            temp1 = front.next
            temp2 = prev.next
            front.next = prev
            prev.next = temp1
            if temp1 == None:
                front.next.next = temp2
                break
            front = temp1
            prev = temp2
            
        

            

        




