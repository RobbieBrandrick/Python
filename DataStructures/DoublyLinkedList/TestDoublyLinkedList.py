import unittest
from DoublyLinkedList.LinkedList import LinkedList

class TestDoublyLinkedList(unittest.TestCase):		

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

	def test_iter_2(self):
		list = LinkedList()	    

		for i in range(0, 10):
			list.append(i)

		self.assertEqual(list.count, 10)

		i = 0		
		for v in list:
			self.assertEqual(v, i)
			i += 1

		self.assertEqual(list.count, i)		


	def test_iter_is_not_mutable(self):
		list = LinkedList([1, 2, 3])

		for v in list:
			v = 69

		for i in range(len(list)):
			self.assertNotEqual(list[i], 69)

	def test_setdata(self):
		list = [1, 2, 3]

		for i, v in enumerate(list):
			list[i] = 69

		for i in range(len(list)):
			self.assertEqual(list[i], 69)				

	def test_remove(self):
		
		list = LinkedList()
		
		with self.assertRaises(IndexError):
			list.remove(0)		
		
		list.append(0)
		self.assertEqual(list[0], 0)
		list.remove(0)
		
		with self.assertRaises(IndexError):
			list[0]
		
		list = LinkedList()	    
		for i in range(0, 10):
			list.append(i)	    	
		
		self.assertEqual(list[5], 5)
		
		list.remove(5)
		for data in list:
			self.assertNotEqual(data, 5)

		with self.assertRaises(IndexError):
			list.remove(999)
			
	def test_insert(self):
		list = LinkedList()

		with self.assertRaises(IndexError):
			list.insert(1, 0)		

		list.insert(0, 0)
		self.assertEqual(list[0], 0)
		list.insert(0, 1)
		self.assertEqual(list[0], 1)	

		list.insert(2, 2)
		self.assertEqual(list[0], 1)	
		self.assertEqual(list[1], 0)	
		self.assertEqual(list[2], 2)	

		list.insert(2, 3)
		list.insert(2, 4)
		self.assertEqual(list[0], 1)	
		self.assertEqual(list[1], 0)	
		self.assertEqual(list[2], 4)			
		self.assertEqual(list[3], 3)			
		self.assertEqual(list[4], 2)			

		with self.assertRaises(IndexError):
			list.insert(6, 3)	

	def test_count(self):
		list = LinkedList()	    

		self.assertEqual(list.count, 0)

		for i in range(0, 10):
			list.append(i)	  

		self.assertEqual(list.count, 10)

	def test_front_back(self):
		list = LinkedList()	    

		for i in range(0, 10):
			list.append(i)	  
			self.assertEqual(list.front(), 0)
			self.assertEqual(list.back(), i)

		for i in range(0, 10):
			list.prepend(i)	  
			self.assertEqual(list.front(), i)
			self.assertEqual(list.back(), 9)	

	def test_remove_front_back(self):
		list = LinkedList()	    

		for i in range(0, 10):
			list.append(i)

		self.assertEqual(list.count, 10)

		while len(list) > 0:
			self.assertEqual(list.back(), 9)
			list.remove_front()

		self.assertEqual(list.count, 0)

		for i in range(0, 10):
			list.append(i)

		self.assertEqual(list.count, 10)

		while len(list) > 0:
			self.assertEqual(list.front(), 0)
			list.remove_back()

		self.assertEqual(list.count, 0)

	def test_get_node(self):
		list = LinkedList([1, 2, 3])    

		self.assertEqual(list.get_node(2).data, 3)
		self.assertEqual(list.get_node(1).data, 2)
		self.assertEqual(list.get_node(0).data, 1)

		list.append(10)
		self.assertEqual(list.get_node(3).data, 10)

		list.prepend(10)
		self.assertEqual(list.get_node(0).data, 10)		

unittest.main()
