"""
wilsons theorem
n-1! = -1 mod n
"""

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def check_primes(n):
    return factorial(n-1) % n != 0

def generate_primes(amount_to_gen):
    to_return = [2]
    tmp = 3
    while len(to_return) < amount_to_gen:
        if check_primes(tmp) == True:
            to_return.append(tmp)
        tmp += 2
    return to_return

print(generate_primes(500))
