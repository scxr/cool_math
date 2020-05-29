import math
"""
Find fibonacci numbers in O(1) time, can be shortened to one liner but extended for readabilaty
The one liner would be math.pow(((1 + math.sqrt(5)) / 2), tofind) / math.sqrt(5)
"""
def fib(tofind):
    phi = ((1 + math.sqrt(5)) / 2)
    return math.floor(math.pow(phi, tofind) / math.sqrt(5))
print(fib(110))
