#!/usr/bin/python
from math import sqrt
import math
from string import ascii_uppercase

from hrank_lib import *

# HACKERRANK Project Euler+ challenges (21-40)

# PROBLEM 21
def prime_factors(n):
    if n == 1:
        return 1

    # Get the prime powers of n
    powers = {}
    i = 2

    while n and i < sqrt(n) + 1:
        if n%i == 0:
            if i in powers:
                powers[i] = powers[i] + 1
            else:
                powers[i] = 1
            n = n/i
        else:
            i = i + 1

    if n > 1:
        if n in powers:
            powers[n] = powers[n] + 1
        else:
            powers[n] = 1

    l = []
    for i in powers.keys():
        l.append((i, powers[i]))

    return l

def divisors(n):
    yield 1

    largest = int(math.sqrt(n))

    # special-case square numbers to avoid yielding the same divisor twice
    if largest * largest == n:
        yield largest
    else:
        largest += 1

    # all other divisors
    for i in range(2, largest):
        if n % i == 0:
            yield i
            yield n / i

def divisor_gen(n):
    factors = prime_factors(n)

    # Create list of divisors.
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

div_sum = {}
div_sum[1] = 0
div_sum[0] = 0

def amicable_numbers(n):
    for i in range(2, n):
        div_sum[i] = sum(list(divisor_gen(i))[:-1])

    return

    l = set()
    for i in range(2, n):
        if i == div_sum[i] or div_sum[i] >= n:
            continue

        if div_sum[div_sum[i]] == i:
            if i < div_sum[i]:
                l.add(sum([i, div_sum[i]]))

    print sum(l)

def amicable_numbers_prob():
    get_input1()

    for v in dict.values():
        amicable_numbers(v)

# PROBLEM 22
def name_value(s):
    s = s.strip()
    return sum(ascii_uppercase.index(c) + 1 for c in s.strip('"'))
        
def name_scores_prob():
    f = open("n.txt")
    s = f.readline().split(',')
    s.sort()

    print sum(i*name_value(s) for i, s in enumerate(s, 1))

# PROBLEM 23
abundant = {}

def is_abundant(n):
    if n < 12:
        return False

    l = list(divisor_gen(n))[:-1]
    return sum(l) > n

def non_abundant_sums(n):
    global abundant

    if n > 28123:
        print "YES"
        return True

    for num in abundant:
        if num > n:
            print "NO"
            return False

        if n - num in abundant:
            print "YES"
            return True

    print "NO"
    return False
    
def non_abundant_sums_prob():
    global abundant

    for i in range(12, 28124):
        if is_abundant(i):
            abundant[i] = True

    sum = 0
    for i in range(28124):
        if not non_abundant_sums(i):
            sum = sum + i

    print sum

    get_input1()

    for v in dict.values():
        non_abundant_sums(v)

# PROBLEM 24
def lex_permutations_2nd(s, k):
    st = [c for c in s]
    st.sort()

    pos_in_bucket = -1
    perm = []
    tot_elems = len(st)

    while len(st) > 2:
        tot_elems = len(st)
        tot_perms = factorial_impl(tot_elems) # N!
        elem_per_bucket = factorial_impl(tot_elems-1) # N!/N = (N-1)!

        # Bucket of Kth permutation
        kth_bucket = (k-1)/elem_per_bucket

        # First char in permutation
        perm.append(st[kth_bucket])

        # Remove the character from the list. And create
        # sub problem.
        st.remove(st[kth_bucket])
        k = k%elem_per_bucket

    if k == 1:
        perm.append(st[0])
        perm.append(st[1])
    else:
        perm.append(st[1])
        perm.append(st[0])

    print str(''.join(perm))

def lex_permutations(s, n):
    st = [c for c in s]
    st.sort()

    done = False
    count = 0
    while not done:
        count = count + 1

        if count == n:
            print str(''.join(st))
            return

        # Find the largest k such that st[i] < st[i+1]. That is to
        # say find the right most character which is smaller than
        # the next character. If not found we have all elements in 
        # decreasing order so we are done.
        k = -1
        for i in range(0, len(st)-1):
            if st[i] < st[i+1]:
                k = i

        if k == -1:
            done = True
            continue

        # Find the largest index l greater than k such that a[k] < a[l].
        # This finds the smallest character > a[k] to the right of a[k].
        l = k+1 
        for i in range(k+1, len(st)):
            if st[i] > st[k] and st[i] < st[l]:
                l = i

        # Swap l and k found above.
        st[l], st[k] = st[k], st[l]

        # Reverse from k+1 to end. And repeat
        t = st[:k+1]
        v = st[k+1:]
        v.reverse()
        st = t + v

def lex_permutations_prob():
    #s = str(raw_input())
    s = "abcdefghijklm"
    get_input1()

    for v in dict.values():
         #lex_permutations(s, v)
         lex_permutations_2nd(s, v)

# PROBLEM 25
def ndigit_fibonacci(n):
    f_num = 0
    for f in fibonacci_gen():
        f_num = f_num + 1
        if len(str(f)) >= n:
            break

    print f_num

def ndigit_fibonacci_prob():
    get_input1()

    for v in dict.values():
        ndigit_fibonacci(v)

# PROBLEM 26
def reciprocal_digit_gen(k, n):
    if k >= n:
        return

    # Generate the next reciprocal digit. Multiply by 10 and divide by
    # N. Use the mod in the next iteration for the next reciprocal.
    while k:
        # Return the reciprocal and remainder
        yield k*10/n, k*10%n
        k = k*10%n

def reciprocal_cycles(n):
    reciprocal = []
    remainder = [1]

    # Check first million reciprocal digits
    cycle_found = False

    for rec, rem in reciprocal_digit_gen(1, n):
        reciprocal.append(rec)

        # There is a cycle if we see the same remainder again
        if rem in remainder:
            cycle_found = True
            break

        remainder.append(rem)

    s_rec = ''.join(map(str, reciprocal))

    if cycle_found:
        i = remainder.index(rem)
        #print n, '0.' + s_rec[:i] + '(' + s_rec[i:] + ')'
        return len(s_rec[i:])
    else:
        #print n, '0.' + s_rec
        return 0


cycles = {}
def reciprocal_cycles_prob():
    get_input1()

    for v in dict.values():
        max_i = 0
        max = -1
        for i in prime_sieve(v+1):
        #for i in range(2, v+1):
            if i in cycles:
                m = cycles[i]
            else:
                m = reciprocal_cycles(i)
                cycles[i] = m

            if m > max:
                max_i = i
                max = m

        print max_i

# PROBLEM 27
def quadratic_primes(THRESHOLD):
    coeff = {}

    # N**2 + a*N + b must produce a prime. N starts at 0.
    # |a| <= THRESHOLD, |b| <= THRESHOLD
    max_a = max_b = max = -1
    for a in range(-THRESHOLD, THRESHOLD+1):
        for b in range(-THRESHOLD, THRESHOLD+1):
            n = 0
            while True:
                v = n*n + n*a + b
                if n < 0 or not is_prime(v):
                    break
                n = n + 1

            if n != 0:
                #coeff[a, b] = n
                if n > max:
                    max_a = a
                    max_b = b
                    max = n

    print max_a, max_b

def quadratic_primes_prob():
    num = int(raw_input())
    quadratic_primes(num)

# PROBLEM 28
def num_spiral_diagonals2(n):
    '''
    sum = 1
    for i in xrange(3, n+1, 2):
        sum = sum + 4*(i*i) - 6*i + 6
    '''

    sum = (4*(n**3) + 3*(n**2) + 8*n - 9)/6
    print sum

def num_spiral_diagonals(n):
    sum = num = 1
    for j in range(1, n/2+1):
        prev = num
        for i in range(1, 5):
            num = prev + (2*j)*i
            sum = sum + num
    
    print sum

def num_spiral_diagonals_prob():
    get_input1()

    for n in dict.values():
        num_spiral_diagonals2(n)

# PROBLEM 29
def distinct_power_prob():
    n = int(raw_input())
    print len(set(a**b for a in range(2, n+1) for b in range(2, n+1)))

# PROBLEM 30
def powern_sum(a, n):
    sum = 0
    while a:
        #print a, n, sum
        sum = sum + int(pow(a%10, n))
        a = a/10

    return sum

def nth_power_num_prob():
    n = int(raw_input())

    tsum = 0
    for num in range(2, 600000):
        s = powern_sum(num, n)
        if num == s:
            tsum = tsum + s
            print s

    print tsum 

# PROBLEM 31
coins = {}
def coin_sums(denom, num):
    list = []
    
    for i in denom:
        if i <= num:
            #list.append((num, i, [i]))
            list.append((num, i))

    count = 0
    while len(list):
        #n, d, l = list.pop()
        n, d = list.pop()

        if (n,d) in coins:
            count = count + coins[n,d]

        if n == d:
            count = count + 1
            #print l
            continue

        if n - d == 0:
            count = count + 1
            #print l
            continue
       
        if n - d < 0:
            continue

        for j in denom:
            if j <= d:
                #list.append((n - d, j, l + [j]))
                list.append((n - d, j))

    print count

def coin_sums_rec(denom, num, l):
    if num == 0:
        return 1

    count = 0

    for d in denom:
        if num - d < 0:
            break
        count = count + coin_sums_rec(denom, num - d, l+[d])

    return count

def coin_sums_dynamic_prog(denom, num):
    count = [0]*(num+1)
    count[0] = 1

    for d in denom:
        for n in range(d, num+1):
            count[n] = count[n] + count[n - d]

    print count[num]

def coin_sums_prob():
    global count
    denom = [1, 2, 5, 10, 20, 50, 100, 200]

    get_input1()

    for n in dict.values():
        #coin_sums(denom, n)
        print coin_sums_rec(denom, n, [])
        #coin_sums_dynamic_prog(denom, n)

# PROBLEM 32
def is_pandigital(n, k):
    r = []
    for i in range(1, k+1):
        r.append(str(i))

    r.sort()
    s = [c for c in n]
    s.sort()

    return r == s

def pandigital_product(n):
    r = []
    for i in range(1, n+1):
        r.append(i)

    # For n digits. The product has to be within pow(n/2, 10).
    # Check factors for pandigital.

    s = []
    for i in range(1, pow(10, n/2)):
        for j in range(1, i+1):
            if i%j == 0:
                num = str(i)+str(j)+str(i/j)
                if is_pandigital(num, n) and not i in s:
                    s.append(i)
                    #print i, j, i/j, num

    print sum(s)

def pandigital_product_prob():
    num = int(raw_input())

    pandigital_product(num)

# PROBLEM 33
def digit_cancelling_fractions(n, k):
    for i in range(1, pow(10, n)):
        for j in range(1, i):

def digit_cancelling_fractions_prob():
    n = int(raw_input())
    k = int(raw_input())

    digit_cancelling_fractions(n, k)

if __name__ == "__main__":
    digit_cancelling_fractions_prob()

    '''
    pandigital_product_prob()

    coin_sums_prob()

    nth_power_num_prob()

    distinct_power_prob()

    num_spiral_diagonals_prob()

    quadratic_primes_prob()

    reciprocal_cycles_prob()

    ndigit_fibonacci_prob()

    lex_permutations_prob()

    non_abundant_sums_prob()

    name_scores_prob()

    amicable_numbers_prob()
    '''
