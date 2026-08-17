class Node:

    def __init__ (self, data: int):
        self.data = data
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.m = dict()
        self.length = 0

        

    def get(self, key: int) -> int:
        if key in self.m:
            node = self.m[key]

            print(self.m)
            if not self.head.next == node:
                back = node.prev
                nex = node.next

                back.next = node.next
                back.next.prev = back

                node.next = self.head.next
                node.next.prev = node

                self.head.next = node
                node.prev = self.head

            return node.data[1]
        return -1

        

    def put(self, key: int, value: int) -> None:

        newNode = Node((key,value))

        newNode.next = self.head.next
        self.head.next = newNode

        newNode.next.prev = newNode
        newNode.prev = self.head

        if not key in self.m: 
            self.length += 1

            if self.length > self.capacity:

                last = self.tail.prev

                print(self.m)
                self.m.pop(last.data[0])

                self.tail.prev = last.prev
                last.prev.next = self.tail

                self.length-=1
        else:
            prevNode = self.m[key]
            prevNode.prev.next = prevNode.next
            prevNode.next.prev = prevNode.prev

        self.m[key] = newNode


            

            

        
