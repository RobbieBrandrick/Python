from collections import deque

class Node:
	
	def __init__(self, value, nodes):
		self.value = value
		self.nodes = nodes
		self.visited = False
		
		
def bfs(node):
	
	queue = deque()
	
	queue.append(node)
	
	while len(queue) > 0:
		
		r = queue.popleft()
		
		if r.visited == True:
			continue
			
		r.visited = True
		
		print(r.value)
		
		for n in r.nodes:
			queue.append(n)
	
			
n5 = Node(5, [])
n4 = Node(4, [n5])
n3 = Node(3, [n4])
n2 = Node(2, [n3])
n1 = Node(1, [n2, n4])


bfs(n1)