class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head):
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev