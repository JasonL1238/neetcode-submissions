# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            print(lists[0].val)
            return lists[0]
        elif len(lists) > 2:
            half = len(lists)//2
            node1 = self.mergeKLists(lists[0:half])
            node2 = self.mergeKLists(lists[half:])
            return self.mergeKLists([node1,node2])
        else:
            head1 = lists[0]
            head2 = lists[1]

            dummy = ListNode()
            tail = dummy

            while not head1 == None and not head2 == None:

                if head1.val < head2.val:
                    tail.next = head1
                    head1 = head1.next
                else:
                    tail.next = head2
                    head2 = head2.next
                tail = tail.next
            
            if head1 == None:
                tail.next = head2
            else:
                tail.next = head1
            
            return dummy.next




            
            return dummy

                    
                        
                    




        
