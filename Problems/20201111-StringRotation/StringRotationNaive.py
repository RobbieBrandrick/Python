import unittest

def is_rotation(s1, s2):

	if len(s1) != len(s2):
		return False

	c = s1[0]
	if c not in s2:
		return False
		
	for i in range(len(s2)):
		
		if c == s2[i]:
			if compare_indexes(s1, s2, i):
				return True
				
	return False
	
def compare_indexes(s1, s2, i):
		
	for j in range(len(s2)):
		
		if s1[j] != s2[i]:
			return False
			
		i += 1
		
		if i >= len(s2):
			i = 0
			
	return True
	
class TestStringRotation(unittest.TestCase):
	
	def test_positive_1char_case(self):
		s1 = "a"
		s2 = "a"
		
		self.assertTrue(is_rotation(s1, s2))
		
	def test_positive_2char_case(self):
		s1 = "ab"
		s2 = "ba"
		
		self.assertTrue(is_rotation(s1, s2))
		
	def test_positive_2char2_case(self):
		s1 = "ab"
		s2 = "ab"
		
		self.assertTrue(is_rotation(s1, s2))
	
	def test_positive_case(self):
		s1 = "waterbottle"
		s2 = "erbottlewat"
		
		self.assertTrue(is_rotation(s1, s2))
		
	def test_positive_case_2(self):
		s1 = "waterwottle"
		s2 = "erwottlewat"
		
		self.assertTrue(is_rotation(s1, s2))
		
	def test_positive_case_2(self):
		s1 = "aterwottlew"
		s2 = "erwottlewat"
		
		self.assertTrue(is_rotation(s1, s2))
		
	def test_negative_case(self):
		s1 = "waterbottle"
		s2 = "arbottlewat"
		
		self.assertFalse(is_rotation(s1, s2))
		
	def test_negative_2_case(self):
		s1 = "waterbottle"
		s2 = "arbottleweat"
		
		self.assertFalse(is_rotation(s1, s2))
		
	def test_negative_different_lengths_case(self):
		s1 = "waterbottle"
		s2 = "rbottlewat"
		
		self.assertFalse(is_rotation(s1, s2))	
		
unittest.main()