def is_pal(n):
	"Returns if an int is a palindrome number or not"
	
	n = str(n)
	start_ptr = 0
	end_ptr = len(n) - 1
	
	while start_ptr < end_ptr:
		if n[start_ptr] != n[end_ptr]:
			return False
		else:
			start_ptr = start_ptr + 1
			end_ptr = end_ptr - 1
	
	return True

a = 999
b = 999

n = a * b # biggest possible number

possibles = []

while n > 0:
	if is_pal(n):
		possibles.append(n) # the biggest possible for this a has been found, save it and start over
		a = a - 1
		b = 999
	elif b == 0:
		a = a - 1
		b = 999
	else:
		b = b - 1 
	
	n = a * b
		
print max(possibles)

