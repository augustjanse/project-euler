import math

i = 1
n = 100

sum_ = 0
while i <= n:
	sum_ += i**2
	i += 1

sq = 0
i = 1	
while i <= n:
	sq += i
	i += 1
sq = sq**2

print abs(sum_ - sq)
