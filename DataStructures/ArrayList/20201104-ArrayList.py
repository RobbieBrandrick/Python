import unittest

class ArrayList:
	
	def __init__(self, size = 16):
		self._list = [None]*size
		self._index = 0
		
	def __str__(self):
		return "[{}]".format(", ".join(str(i) for i in self._list if i != None))
	
	def append(self, value):
		
		if self._index >= len(self._list):
			newList = [None] * len(self._list) * 2
			
			for i in range(0, len(self._list)):
				newList[i] = self._list[i]
				
			self._list = newList
				
		self._list[self._index] = value
		
		self._index += 1
		
	def __getitem__(self, i):
		
		if i >= self._index:
			return None
			
		return self._list[i]
		
	def __setitem__(self, i, value):
		
		if i >= self._index:
			raise IndexError('Index out of range')
		
		self._list[i] = value

class TestArrayList(unittest.TestCase):
	
	def test_one_element_array(self):
		arrayList = ArrayList(1)
		
		arrayList.append(1)
		
		self.assertEqual(arrayList[0], 1)
		self.assertEqual(arrayList[1], None)
		
		arrayList[0] = 10
		
		self.assertEqual(arrayList[0], 10)
		
		with self.assertRaises(IndexError):
			arrayList[1] = 10
		
	def test_multielement_array(self):
		list = ArrayList()
		
		for i in range(0, 100):
			list.append(i)
			self.assertEqual(list[i], i)

		list[0] = 100
		self.assertEqual(list[0], 100)

		list[99] = 100
		self.assertEqual(list[99], 100)		

		with self.assertRaises(IndexError):
			list[100] = 10		
	
unittest.main()

# list = ArrayList()

# for i in range(0, 100):
# 	list.append(i)	

# print(list)