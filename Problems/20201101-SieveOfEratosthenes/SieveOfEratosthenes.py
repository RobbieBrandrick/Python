def SieveOfEratosthenes(n):
	
	sieve = [True] * n
	
	i = 1
	
	while i * i <= n:
		
		i += 1
		
		if sieve[i] == False:
			continue
			
		for j in range(i + i, n, i):
			
			sieve[j] = False
			
	return [i for i, s in enumerate(sieve) if s and i > 1]
	
print(SieveOfEratosthenes(100))