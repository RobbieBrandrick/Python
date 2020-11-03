class Node:
	
	def __init__(self, value, nodes):
		self.value = value
		self.nodes = nodes
		self.visited = False
		
def dfs(node):
	
	node.visited = True
	
	print(node.value)
	
	for n in node.nodes:
		
		if n.visited == False:
			dfs(n)
			
n5 = Node(5, [])
n4 = Node(4, [n5])
n3 = Node(3, [n4])
n2 = Node(2, [n3])
n1 = Node(1, [n2, n4])

dfs(n1)