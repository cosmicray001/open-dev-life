class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
     	return self.items.pop() if not self.isEmpty() else 'stack is empty'

     def size(self):
         return len(self.items)
         

if __name__ == '__main__':
	stack = Stack()
	stack.push(1)
	stack.push(2)
	
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())

