# Library functions for HACKERRANK problems

from math import *

dict = {}
def get_input1():
    global dict
    num_vals = int(raw_input())
               
    i = 0
    for i in range(0, num_vals):
        dict[i] = int(raw_input())

primes = []
def prime_sieve(n):
    global primes
           
    primes = []
               
    a = [True]*(n+1)
    a[0] = a[1] = False

    for i in range(2, sqrt(n)+1):
        # Find first prime to strike.
        if not a[i]:
            continue
        for j in xrange(2*i, n+1, i):
            a[j] = False

    for i in range(2, n+1):
        if a[i]:
            primes.append(i)

    return primes

primes_bool = {}
def is_prime(n):
    global primes_bool

    if n in primes_bool:
        return primes_bool[n]

    if n < 2:
        return False

    if n ==2 or n == 3:
        primes_bool[n] = True
        return True

    if n%2 == 0 or n%3 == 0 or n%5 == 0:
        return False

    i = 7
    while i*i <= n:
        if n%i == 0:
            return False
        i = i + 2

    primes_bool[n] = True
    return True

def factorial_impl(n):
    return reduce(lambda x,y:x*y, range(1,n+1))

def fibonacci_gen():
    # F(1) = 1, F(2) = 1
    yield 1
    yield 1

    f1 = f2 = 1
    while True:
        f1, f2 = f2 + f1, f1
        yield f1

def gcd(a, b):
    while b:
        a, b = b, a%b

    return a

def lcm(a, b):
    return (a/gcd(a,b))*b
