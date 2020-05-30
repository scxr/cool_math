"""
Chudnovksy algorithm is an algorithm designed by the Chudnovksy brothers, the formula is as follows:
1/pi = 12(infite series)(-1)^k(6k)!(545140134k + 13591409)/(3k)!(k1)^3(640320)^3k+3/2
which for computational purposes can be simplified to
426880*sqrt(10005)/(infinite series) (6k)!(545140134k + 13591409)/(3k)!(k!)^3(-26253741264078000)^k
an in depth description can be found at : https://en.wikipedia.org/wiki/Chudnovsky_algorithm
"""
import math
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def find_pi(k: int = 0): # we default the value to 0 if one isnt passed for any reason
    # (6k)!(545140134k + 13591409)/(3k)!(k!)^3(-26253741264078000)^k
    a = factorial(6*k)
    b = (545140134 * k) + 13591409
    c = factorial(3*k)
    d = factorial(k) ** 3
    e = (-26253741264078000) ** k
    numerator = a *b
    print(numerator)
    print(e)
    denominator = c*d*e
    res = numerator/denominator
    new_numerator = 426880*math.sqrt(10005)
    return new_numerator / res

find_pi()
