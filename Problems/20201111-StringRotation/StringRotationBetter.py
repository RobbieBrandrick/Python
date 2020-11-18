import unittest

def is_rotation(s1, s2):
	return is_substring(s2 + s2, s1)
	
def is_substring(str, subStr):
	i = str.index(subStr[0])
	
	while i + len(subStr) < len(str):
		if str[i:len(subStr) + i] == subStr:
			return True
			
		i += str.index(subStr[0], i)
			
	return False
	

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
		
	def test_positive_case_3(self):
		s1 = "waterwottle"
		s2 = "wottlewater"
		
		self.assertTrue(is_rotation(s1, s2)
		
	def test_positive_case_4(self):
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