import unittest
from DoublyLinkedList.LinkedList import LinkedList

def is_palindrome(l):
	list = l.copy()
	loops = int(len(list) / 2)
	for i in range(loops):
		if list.front() != list.back():
			return False
		
		list.remove_front()
		list.remove_back()
		
	return True
		
class TestIsPalindrome(unittest.TestCase):
	
	def test_is_palindrome(self):
		
		l = LinkedList()
		
		l.append("l")
		
		self.assertTrue(is_palindrome(l))
		
		l.append("o")
		
		self.assertFalse(is_palindrome(l))
		
		l.append("l")
		
		self.assertTrue(is_palindrome(l))
		
		l.clear()
		
		l.append("b")
		l.append("o")
		l.append("o")
		l.append("b")
		
		self.assertTrue(is_palindrome(l))
		
		l.append("s")
		
		self.assertFalse(is_palindrome(l))		
unittest.main()