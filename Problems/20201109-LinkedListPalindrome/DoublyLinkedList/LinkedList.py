from DoublyLinkedList.Node import Node

class LinkedList:
	
	def __init__(self, l = None):
		self.clear()
		
		if l is not None:
			self.append_list(l)
		
	def __iter__(self):
		node = self.head.next

		while node != self.head:
			yield node.data
			node = node.next
		
	def __getitem__(self, n):
		node = self.get_node(n)

		if node == self.head:
			raise IndexError('Index out of range')		
			
		return node.data
		
	def __setitem__(self, n, value):
		node = self.get_node(n)

		node.data = value
		
	def __len__(self):
		return self.count

	def __str__(self):
		return ", ".join([str(value) for value in self]).join(("[", "]"))

	def __repr__(self):
		return str(self)
		
	def prepend(self, value):
		newNode = Node(value, self.head, self.head.next)
		self.head.next.prev = newNode
		self.head.next = newNode
		self.count += 1

	def prepend_list(self, l):
		for v in l:
			self.prepend(v)				
		
	def append(self, value):
		newNode = Node(value, self.head.prev, self.head)
		self.head.prev.next = newNode
		self.head.prev = newNode
		self.count += 1

	def append_list(self, l):
		for v in l:
			self.append(v)		

	def insert(self, n, value):

		if n > self.count:
			raise IndexError('Index out of range')

		node = self.get_node(n)		
		newNode = Node(value, node.prev, node)
		node.prev.next = newNode
		node.prev = newNode
		self.count += 1		

	def remove(self, n):
		node = self.get_node(n)

		if node == self.head:
			raise IndexError('Index out of range')

		prevNode = node.prev
		nextNode = node.next
		prevNode.next = nextNode
		nextNode.prev = prevNode
		self.count -= 1

	def remove_front(self):
		n = self.head.next
		self.head.next = n.next
		n.next.prev = self.head
		self.count -= 1
		
	def remove_back(self):
		n = self.head.prev
		self.head.prev = n.prev
		n.prev.next = self.head
		self.count -= 1		
		
	def front(self):
		return self.head.next.data
		
	def back(self):
		return self.head.prev.data
		
	def clear(self):
		self.head = Node()		
		self.head.prev = self.head
		self.head.next = self.head
		self.count = 0
		
	def copy(self):
		newList = LinkedList()
		
		for v in self:
			newList.append(v)
			
		return newList

	def get_node(self, n):
		node = self.head
		for i in range(0, n + 1):
			node = node.next
			if node == self.head:
				break
			
		return node		


l = LinkedList([1, 2, 3])
print(l)		