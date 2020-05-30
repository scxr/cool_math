"""
Find fibonacci numbers in O(1) time
"""

def fib(tofind):
	phi = (1 + (5 ** 0.5)) / 2
	if tofind % 2 == 0:
		return int((phi ** tofind) / (5 ** 0.5))
	else:
		return int(((phi ** tofind) / (5 ** 0.5)) + 1)

print(fib(110))
