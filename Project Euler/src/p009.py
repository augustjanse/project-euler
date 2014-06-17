# a^2 + b^2 = c^2
# a + b + c = 1000
# 0 < a < b < c < 1000

c = 334
c_list = []
while c <= 1000:
	c_list.append(c)
	c += 1

b = 334
b_list = []
while b <= 1000:
	b_list.append(b)
	b += 1

a = 1
a_list = []
while a <= 333:
	a_list.append(a)
	a += 1

def loop():
	for c in c_list: # O(n^3)
		for b in b_list:
			for a in a_list:
				if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
					return [a, b, c]

answers = loop()
print answers[0] * answers[1] * answers[2]
