from random import choice

def get_hash_collision():
	ascii = [chr(i) for i in range(33, 127)]
	
	dict = {}
	for i in range(0, 1000000):
		value = ''.join([choice(ascii) for _ in range(100)])
		key = hash(value)
		if key not in dict:
			dict[key] = value
		else:
			if dict[key] == value:
				continue
				
			return value, dict[key]
			
	raise Exception("No duplicate hash found")
	
if __name__ == "__main__":
	v1, v2 = get_hash_collision()
	print(v1, v2)