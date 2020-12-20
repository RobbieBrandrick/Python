from DoublyLinkedList.LinkedList import LinkedList

class HashMap:
	def __init__(self, size = 4):
		self.list = [None]*size
		self.count = 0
		
	def hash(self, key):
		return hash(key) % len(self.list)

	def __getitem__(self, key):
		return self.get(key)
		
	def __setitem__(self, key, value):
		self.add(key, value)

	def get(self, key):
		
		index = self.hash(key)
		
		if self.list[index] is None:
			raise KeyError("Cannot Find Key")
			
		for kvp in self.list[index]:
			if kvp[0] == key:
				return kvp[1]
					
		raise KeyError("Cannot Find Key")

	def add(self, key, value):
		self.expand()
		
		index = self.hash(key)
		
		if self.list[index] is None:
			
			self.list[index] = LinkedList()
			self.list[index].append([key, value])
		
		else:
			
			for kvp in self.list[index]:
				if kvp[0] == key:
					kvp[1] = value
					break
			else:
				self.list[index].append([key, value])
		
		self.count += 1
				
	def remove(self, key):
		index = self.hash(key)
		
		if self.list[index] is None:
			raise KeyError("Cannot Find Key")
		
		for i, kvp in enumerate(self.list[index]):
			if kvp[0] == key:
				self.list[key].remove(i)
				self.count -= 1
				return
				
		raise KeyError("Cannot Find Key")
					
	def expand(self):
		if self.is_full():
			self.double_map_size()
	
	def is_full(self):
		return self.count > (len(self.list) / 2) 
					
	def double_map_size(self):
		map = HashMap(len(self.list) * 2)
		
		for linkedList in self.list:
			
			if linkedList is None:
				continue
				
			for kvp in linkedList:
				map.add(kvp[0], kvp[1])
			
		self.list = map.list