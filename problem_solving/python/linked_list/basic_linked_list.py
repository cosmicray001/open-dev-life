class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNode:

    def __init__(self):
        self.head = self.tail =None

    def insert(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def travarse(self):
        tmp_head = self.head

        while tmp_head:
            print("Current Node Value {}".format(tmp_head.val))
            tmp_head = tmp_head.next


obj = ListNode()
obj.insert(1)
obj.insert(3)
obj.insert(2)
obj.travarse()
    