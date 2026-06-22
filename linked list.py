class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        itr = self.head
        while itr.next:
            
            itr = itr.next
        itr.next = new
    def add_begin(self, data):
        obj= Node(data)
        if self.head is None:
            self.head = obj
            return
        obj.next = self.head
        self.head = obj
    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end='-->')
            itr = itr.next
ll=LinkedList()
ll.add_begin(40)
ll.add_end(50)
ll.add_end(60)
ll.add_end(70)
ll.display()