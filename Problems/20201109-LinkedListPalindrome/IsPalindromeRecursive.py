import unittest
from DoublyLinkedList.LinkedList import LinkedList

def is_palindrome(list):
	return is_palindrome_recursive(list, 0, len(list) - 1)
	
def is_palindrome_recursive(list, begin, end):
	if begin >= end:
		return True
		
	if list[begin] == list[end]:
		return is_palindrome_recursive(list, begin + 1, end - 1)
	else:
		return False
		
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