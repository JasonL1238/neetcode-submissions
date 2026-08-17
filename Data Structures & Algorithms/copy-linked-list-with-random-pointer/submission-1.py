"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        if head == None:
            return None

        dummy = head

        while not dummy == None:
            copy = Node(dummy.val)
            temp = dummy.next
            dummy.next = copy
            copy.next = temp
            dummy = temp

        dummy = head
        while not dummy == None:
            copy = dummy.next
            if dummy.random == None:
                copy.random = None
            else:
                rand = dummy.random.next
                print(rand.val)
                copy.random = rand
            dummy = copy.next

        copy = head.next
        dummy2 = copy
        dummy = head
        while not copy.next == None:
            dummy.next = dummy.next.next
            dummy = dummy.next
            copy.next = copy.next.next
            copy = copy.next
        
        dummy.next = dummy.next.next
        dummy = dummy.next
        return dummy2
























        
