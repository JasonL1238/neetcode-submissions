# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):, no_type_check_decorator
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        groupPrev = ListNode(0,head)
        dummy = self.findKth(groupPrev,k)

        while True:
            kth = self.findKth(groupPrev,k)
            if kth == None:
                break
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next

            
            while not curr == groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            

        if dummy == None:
            return head
        return dummy
    
    def findKth(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = node
        while k > 0 and not dummy == None:
            dummy = dummy.next
            k -= 1
        return dummy


            








