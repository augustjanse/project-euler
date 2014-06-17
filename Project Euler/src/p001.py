i = 1
sum_ = 0

while i < 1000:
	if i % 3 == 0:
		sum_ = sum_ + i
	elif i % 5 == 0:
		sum_ = sum_ + i
	i = i + 1

print sum_
