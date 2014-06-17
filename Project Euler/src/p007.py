def is_prime(n):
	if n == 1:
		return False
	
	for i in primes:
		if n % i == 0:
			return False
	return True
		
i = 1
primes = []
while len(primes) < 10001:
	if is_prime(i):
		primes.append(i)
	i += 1

print primes[10000]


