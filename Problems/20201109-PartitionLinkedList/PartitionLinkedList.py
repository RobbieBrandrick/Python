import unittest
from DoublyLinkedList.LinkedList import LinkedList

def partition(l, x):
	
	min, max = 0, len(l) - 1
	
	while min < max:
		
		while l[min] < x:
			min += 1
			
		while l[max] > x:
			max -= 1
			
		swap(l, min, max)
		min += 1
		max -= 1
		
def swap(l, lhs, rhs):
	temp = l[lhs]
	l[lhs] = l[rhs]
	l[rhs] = temp

class TestPartitionLinkedList(unittest.TestCase):
	
	def test_partition(self):
		
		l = LinkedList([])
		partition(l, 2)
		self.assertEqual(l, [])	

		l = LinkedList([2, 1])
		partition(l, 2)
		self.assertEqual(l, [1, 2])	

		l = LinkedList([1, 2])
		partition(l, 2)
		self.assertEqual(l, [1, 2])			

		l = LinkedList([2, 3, 1])
		partition(l, 2)
		self.assertEqual(l, [1, 3, 2])			

		l = LinkedList([1, 2, 3])
		partition(l, 2)
		self.assertEqual(l, [1, 2, 3])	

		l = LinkedList([1, 2, 3, 4])
		partition(l, 2)
		self.assertEqual(l, [1, 2, 3, 4])		

		l = LinkedList([4, 3, 2, 1])
		partition(l, 2)
		self.assertEqual(l, [1, 2, 3, 4])				

		l = LinkedList([3, 2, 1, 4])
		partition(l, 2)
		self.assertEqual(l, [1, 2, 3, 4])			

		l = LinkedList([3, 2, 1, 4])
		partition(l, 3)
		self.assertEqual(l, [1, 2, 3, 4])			

		l = LinkedList([5, 3, 2, 1, 4])
		partition(l, 3)
		self.assertEqual(l, [1, 2, 3, 5, 4])			

		l = LinkedList([3, 5, 8, 5, 10, 2, 1])
		partition(l, 5)
		self.assertEqual(l, [3, 1, 2, 5, 10, 8, 5])

	
		
unittest.main()
		