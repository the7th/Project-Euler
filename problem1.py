# This is for problem 1 of ProjectEuler https://projecteuler.net/problem=1
n = 0
y = 0
for x in range(1000):
	if (x%5 == 0):
		n = n + x
	if (x%3 == 0):
		y = y + x

print (n+y)