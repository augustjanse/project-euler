primes = []

iterator = 0
while iterator < 20: # create a list of empty lists
	primes.append([])
	iterator = iterator + 1

divisor = 1
while divisor <= 20: # extract all factors of values from 1 to 20
	remainder = divisor
	factor = 2

	while factor < remainder:
		if remainder % factor == 0:
			primes[divisor-1].append(factor)
			remainder = remainder / factor
			factor = 2
		else:
			factor += 1
			
	primes[divisor-1].append(remainder) # the remainder is the last factor
	divisor = divisor + 1
	
print primes

iterator = 0
factors = []
while iterator < 20: # for each sublist
	factor = 0
	while factor <= 20: # for each possible factor in the list
		if primes[iterator].count(factor) > factors.count(factor): # if the sublist has more of the factor
			i = 0
			while i < primes[iterator].count(factor) - factors.count(factor): # add the difference
				factors.append(factor)
				i += 1
		factor += 1
	iterator += 1
	
print factors

product = 1
for factor in factors: # multiply together all factors
	product = product * factor
				
print product
