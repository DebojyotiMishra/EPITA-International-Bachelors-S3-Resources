class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = -1
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = 1
        self.tail = -1
        self.size = 0
    
    def add(self, value):
        node = LinkedListNode(value)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1