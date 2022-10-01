'''
    This program will detect if a linked list has a cycle or not
    test case 1 -> 1->2->3->4->2 this has a cycle
    test case 2 -> 1->2->3->4 this doesn;t have cycle

    Soultion is O(n) with no extra space
'''

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def has_cycle(self, head):
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False


head = node = Node(1)
node_two = node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = node_two

print(Solution().has_cycle(head))