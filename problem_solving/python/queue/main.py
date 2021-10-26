class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop() if not self.isEmpty() else 'queue is empty'

    def size(self):
        return len(self.items)
        
if __name__ == '__main__':
	queue = Queue()
	queue.enqueue(1)
	queue.enqueue(2)
	
	print(queue.dequeue())
	print(queue.dequeue())
	print(queue.dequeue())
