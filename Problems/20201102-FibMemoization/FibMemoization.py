def fib(n, memo):
	if n == 1 or n == 0:
		return n
		
	if n not in memo:
		memo[n] = fib(n - 1, memo) + fib(n-2, memo)

	return memo[n]

memo = {}

for i in range(0, 100):
	print('fib(', i, '):', fib(i, memo))

