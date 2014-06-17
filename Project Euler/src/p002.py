sum_ = 0
prev, curr = 1, 2

while curr <= 4000000:
	if curr % 2 == 0:
		sum_ = sum_ + curr
	prev, curr = curr, curr + prev
	
print sum_
