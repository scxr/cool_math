"""
Chudnovksy algorithm is an algorithm designed by the Chudnovksy brothers, the formula is as follows:
1/pi = 12(infite series)(-1)^k(6k)!(545140134k + 13591409)/(3k)!(k1)^3(640320)^3k+3/2
which for computational purposes can be simplified to
426880*sqrt(10005)/(infinite series) (6k)!(545140134k + 13591409)/(3k)!(k!)^3(-26253741264078000)^k
an in depth description can be found at : https://en.wikipedia.org/wiki/Chudnovsky_algorithm
"""
import math
from decimal import Decimal as decimal, getcontext as gc

def chudnovksy(max_k : int, precision : int):
    gc().prec = precision
    k = 6
    m = 1
    l = 13591409
    res = 13591409
    x = 1
    l_add = 545140134
    x_mult = -2625327412640768000
    while k < max_k:
        m = k ** 3 - 16 * k // k ** 3 # mk+1 is defined as K^3 - 16K div k^3 where m0 = 1
        l += l_add # l(subscript)k is defined as l(sub)k + 545140134 where l0 = 13591409
        x *= x_mult # x(sub)k is defined as x(sub)k * -2625327412640768000 where x0 = 1
        res += decimal(m*l) / x
        k += 12
    pi = 426880 * decimal(10005).sqrt() / res
    return pi

