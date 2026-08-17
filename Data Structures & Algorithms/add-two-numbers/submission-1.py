# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = l1
        val1 = 0
        head2 = l2
        val2 = 0
        i = 0
        while not head1 == None or not head2 == None:
            if not head1 == None:
                val1 += (10 ** i) * head1.val
                head1 = head1.next
            if not head2 == None:
                val2 += (10 ** i) * head2.val
                head2 = head2.next
            i+=1
        
        total = val1 + val2
        print(total)
        if total == 0:
            return ListNode(0)
        output = ListNode()
        head = output
        while total > 0:
            val = total%10
            total = total//10
            node = ListNode(val)
            output.next = node
            output = output.next
            
        return head.next
