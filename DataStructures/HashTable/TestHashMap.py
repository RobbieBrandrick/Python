import unittest
from HashMap import HashMap

class TestHashMap(unittest.TestCase):
	
	def test_hash(self):
		map = HashMap()
		
		self.assertEqual(map.hash("abcdef"), hash("abcdef") % 4)
		self.assertEqual(map.hash("a"), hash("a") % 4)
		self.assertEqual(map.hash("b"), hash("b") % 4)
		self.assertEqual(map.hash("c"), hash("c") % 4)
		
	def test_add(self):
		map = HashMap()
		
		for i in range(0, 100):
			map.add(i, i)
			self.assertEqual(map[i], i)
			
		map.add("test", 69)
		self.assertEqual(map["test"], 69)
		
	def test_remove(self):
		map = HashMap()
		
		for i in range(0, 100):
			map.add(i, i)
			self.assertEqual(map[i], i)
			
		for i in range(0, 100):
			map.remove(i)
			with self.assertRaises(KeyError):
				self.assertEqual(map[i], i)
				
	def test_setitem(self):
		map = HashMap()
		
		map["test"] =123 
		self.assertEqual(map["test"], 123)
		
	def test_hash_collision(self):
		#It is quite difficult to generate a collision using the built in hash fuction
		pass
		
		
		
unittest.main()