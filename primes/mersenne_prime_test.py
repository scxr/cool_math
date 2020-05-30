"""
to find my primes i will be using the lucas lehmer method
see here : https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test
"""

def mersenne_prime(p):
    s = 4
    m = (2 ** p) - 1
    for i in range(0,p-2):
        s = ((s**2) - 2) % m
    print(s)
    return s==0

to_test = int(input('Please enter the number to test for mersenne'))
resp = mersenne_prime(to_test)
if resp == True:
    print('Is mersenne prime')
else:
    print('Not mersenne prime')
