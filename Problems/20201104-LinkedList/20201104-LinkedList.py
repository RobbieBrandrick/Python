import unittest

class Node:
	
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

class TestNodes(unittest.TestCase):
		
		def test_node(self):
			
			node = Node(10)
			self.assertEqual(node.data, 10)
			
			node2 = Node(2, node)
			self.assertEqual(node2.data, 2)
			self.assertEqual(node2.next, node)
				
						
class LinkedList:
	
	def __init__(self, list = None):
		self.nodes = None
		self.head = None
		if list is not None:
			node = Node(list[0])
			self.head = node
			for i in range(1, len(list)):
				n = Node(list[i])
				node.next = n
				node = n
				
	def __getitem__(self, n):
		node = self.head
		for i in range(0, n + 1):
			if node is None:
				raise IndexError('Index out of range')
			data = node.data
			node = node.next
			
		return data
		
	def __setitem__(self, n, value):
		node = self.head
		for i in range(0, n + 1):
			if node is None:
				raise IndexError('Index out of range')
			n = node
			node = node.next
			
		n.data = value
										
	def __iter__(self):
		node = self.head
		while node is not None:
			yield node.data
			node = node.next
			
	def append(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
		else:
			n = self.head
			while n.next is not None:
				pass
			n.next = node
			
	def prepend(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
		else:
			node.next = self.head
			self.head = node
			
	def insert(self, n, value):
		 newNode = Node(value)
		 if n == 0:
		 	newNode.next = self.head
		 	self.head = newNode
		 else:
		 	node = self.head
		 	for i in range(0, n - 1):
		 		node = node.next
		 	newNode.next = node.next
		 	node.next = newNode
		 			
			
class TestLinkedList(unittest.TestCase):
	
	def test_init(self):
		linkedList = LinkedList()
		linkedList = ([1, 2, 3])
		
	def test_iteration(self):
		list = [1, 2, 3]
		linkedList = LinkedList(list)
		i = 0
		for n in linkedList:
			self.assertEqual(n, list[i])
			i += 1
			
	def test_append(self):
		linkedList = LinkedList()
		linkedList.append(1)
		self.assertEqual(linkedList[0], 1)
		linkedList.append(2)
		self.assertEqual(linkedList[1], 2)
		with self.assertRaises(IndexError):
			linkedList[2]
			
	def test_prepend(self):
		linkedList = LinkedList()
		linkedList.prepend(1)
		self.assertEqual(linkedList[0], 1)
		linkedList.prepend(2)
		self.assertEqual(linkedList[0], 2)
		self.assertEqual(linkedList[1], 1)
		with self.assertRaises(IndexError):
			linkedList[2]
			
	def test_setitem(self):
		linkedList = LinkedList([1, 7, 3])
		
		linkedList[1] = 11
		
		self.assertEqual(linkedList[1], 11)
		with self.assertRaises(IndexError):
			linkedList[3] = 10
			
	def test_insert(self):
		linkedList = LinkedList()
		linkedList.insert(0, 1)
		self.assertEqual(linkedList[0], 1)
		linkedList.insert(0, 2)
		self.assertEqual(linkedList[0], 2)
		linkedList.insert(1, 3)
		self.assertEqual(linkedList[0], 2)
		self.assertEqual(linkedList[1], 3)
		self.assertEqual(linkedList[2], 1)
		

unittest.main()	