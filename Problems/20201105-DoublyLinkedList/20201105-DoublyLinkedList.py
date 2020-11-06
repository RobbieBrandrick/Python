import unittest

class Node:
	
	def __init__(self, data = None, prev = None, next = None):
		self.data = data
		self.prev = prev
		self.next = next
		
	def Link(self, prev = None, next = None):
		self.prev = prev
		self.next = next
		
class LinkedList:
	
	def __init__(self):
		self.head = Node()
		self.head.Link(self.head, self.head)

	def __iter__(self):
		node = self.head.next

		while node != self.head:
			yield node.data
			node = node.next
		
	def __getitem__(self, n):
		node = self.head.next
		data = node.data
		for i in range(0, n + 1):
			if node == self.head:
				raise IndexError('Index out of range')
			data = node.data
			node = node.next
			
		return data
		
	def prepend(self, value):
		newNode = Node(value, self.head, self.head.next)
		self.head.next.prev = newNode
		self.head.next = newNode
		
	def append(self, value):
		newNode = Node(value, self.head.prev, self.head)
		self.head.prev.next = newNode
		self.head.prev = newNode

	def remove(self, n):
		node = self.head.next
		for i in range(0, n + 1):
			if node == self.head:
				raise IndexError('Index out of range')
			nodeToRemove = node
			node = node.next
		
		nodeToRemove.prev.next = node
		node.prev = nodeToRemove.prev

	def insert(self, n, value):
		node = self.head.next
		for i in range(0, n + 1):
			if node == self.head:
				raise IndexError('Index out of range')			
			node = node.next
		
		node = node.prev
		newNode = Node(n, node.prev, node)
		node.prev.next = node
		

class TestLinkedList(unittest.TestCase):		

	def test_append(self):
	    list = LinkedList()	    
	    for i in range(0, 10):
	    	list.append(i)	    	
	    	self.assertEqual(list[i], i)

	def test_prepend(self):
		list = LinkedList()	    
		for i in range(0, 10):
			list.prepend(i)	    	
			self.assertEqual(list[0], i)			
		self.assertEqual(list[9], 0)

	def test_iter(self):
		list = LinkedList()
		i = 0	
		for data in list:
			self.assertEqual(data, i)

		list = LinkedList()
		list.append(0)
		i = 0
		for data in list:
			self.assertEqual(data, 0)
		
		list = LinkedList()	    
		for i in range(0, 1000):
			list.append(i)
		i = 0			
		for data in list:
			self.assertEqual(data, i)
			i += 1

	def test_remove(self):
		list = LinkedList()	    
		for i in range(0, 10):
			list.append(i)	    	
		
		self.assertEqual(list[5], 5)
		
		list.remove(5)
		for data in list:
			self.assertNotEqual(data, 5)

		with self.assertRaises(IndexError):
			list.remove(999)

unittest.main()