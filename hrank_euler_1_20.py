#!/usr/bin/python
import sys
import string
import math
from math import math
import time
import bisect

from hrank_lib import *

# HACKERRANK Project Euler+ challenges

# PROBLEM 1
def sum_multiple(n, k):
    if n%k == 0:
        last = n/k-1
    else:
        last = n/k

    return (k*last*(last + 1))/2

def sum_multiples35():
    get_input1()

    for v in dict.values():
        print sum_multiple(int(v),3) + sum_multiple(int(v),5) - sum_multiple(int(v),15)

# PROBLEM 2
def fib(n):
    first = 1
    second = 1

    even_sum = 0
    sum = 0

    while (sum < n):
        sum = first + second
        if sum < n and sum % 2 == 0:
            even_sum = even_sum + sum

        first = second
        second = sum

    print even_sum

def even_sum():
    get_input1()

    for v in dict.values():
        fib(v)

# PROBLEM 3
def prime_factor(n):
    '''
    1) Start with 2 divide if not divisible try 3 and so on.
    '''

    i = 2
    factors = []
    while n and i < math.sqrt(n): 
        if n%i == 0:
            n = n/i
            factors.append(i)
            i = 2
        else: 
            i = i + 1

    if n > 1:
        factors.append(n)

    print max(factors)

def prime_factor_prob():
    get_input1()

    for v in dict.values():
        start_time = time.time()
        prime_factor(v)
        print "%f seconds" % (time.time() - start_time)

primes = []
def prime_sieve(n):
    global primes

    primes = []

    a = [True]*(n+1)
    a[0] = a[1] = False

    for i in range(2, n/2):
        # Find first prime to strike.
        if not a[i]:
            continue
        for j in xrange(2*i, n+1, i):
            a[j] = False

    for i in range(2, n+1):
        if a[i]:
            primes.append(i)

# PROBLEM 4
palindrome_list = []

def generate_palindrome(n):
    global palindrome_list

    tmp_list = []
    for i in range(10**(n-1), 10**n - 1):
        for j in range(10**(n-1), 10**n - 1):
            k = i*j
            if k >= 101101 and k < 999*999:
                if is_palindrome(k):
                    tmp_list.append(k)

    palindrome_list = list(set(tmp_list))
    palindrome_list.sort()

def is_palindrome(n):
    rev = 0
    fwd = n

    while (n > 0):
        rem = n % 10
        rev = rev*10 + rem
        n = n/10

    if fwd == rev:
        return True

    return False

def palindrome_prod(n):
    i = bisect.bisect_left(palindrome_list, n)
    if i:
        print palindrome_list[i-1]
    else:
        print palindrome_list[0]

def palindrome_prod_prob():
    start_time = time.time()
    generate_palindrome(3)
    print "%f seconds" % (time.time() - start_time)

    get_input1()

    for v in dict.values():
        palindrome_prod(v)

# PROBLEM 5
def euclid_gcd(a, b):
    while b:
        a, b = b, a%b

    return a

def lcm(a, b):
    return (a/euclid_gcd(a, b))*b

def smallest_multiple(n):
    lcmm = 1
    for i in range(1, n+1):
        lcmm = lcm(lcmm, i)

    print lcmm

def smallest_multiple_prob():
    get_input1()

    for v in dict.values():
        smallest_multiple(v)

# PROBLEM 6
def sum_of_squares(n):
    sqr_sum = (n*(n+1))/2
    sqr_sum = sqr_sum*sqr_sum

    sum_sqr = 0
    for i in range(1, n+1):
        sum_sqr = sum_sqr + i*i

    print sqr_sum - sum_sqr

def sum_of_squares_prob():
    get_input1()

    for v in dict.values():
        sum_of_squares(v)

# PROBLEM 7
def nth_prime(n):
    print primes[n-1]

def nth_prime_prob():
    prime_sieve(1000000)

    get_input1()

    for v in dict.values():
        nth_prime(v)

# PROBLEM 8
def largest_product(n, ll, kk):
    l = int(ll)
    k = int(kk)

    best_prod = -1
    for i in range(0, l-k+1):
        prod = 1
        for j in range(0, k):
            prod = prod * int(n[i+j])

        if prod > best_prod:
            best_prod = prod

    print best_prod

def largest_product_prob():
    num_vals = int(raw_input())
    n = []
    l = []
    k = []
        
    i = 0
    for i in range(0, num_vals):
        s = raw_input()
        a, b = s.split()
        num = str(raw_input())
        n.append(num)
        l.append(a)
        k.append(b)
                            
    for i in range(0, len(n)):
        largest_product(n[i], l[i], k[i])

# PROBLEM 9 (NOT PASSING)
def pythagorean_triplet(n):
    best = []
    for a in range(1, n/3):
        for b in range(1, n/2):
            c = n - a - b
            if a**2 + b**2 == c**2:
                best.append(a*b*c)

    if len(best) != 0:
        print max(best)
    else:
        print -1

def pythagorean_triplet_prob():
    get_input1()

    for v in dict.values():
        pythagorean_triplet(v)

# PROBLEM 10 (NOT PASSING 1 TEST)
max_num = 0
def sum_of_primes(n):
    global max_num

    if n > max_num:
        max_num = n
        prime_sieve(n+1)

    i = bisect.bisect_right(primes, n)

    print sum(primes[:i])

def sum_of_primes_prob():
    get_input1()

    for v in dict.values():
        sum_of_primes(v)

# PROBLEM 11
def largest_product_grid(array, n, k):
    best = -1

    for row in range(n):
        for col in range(n-k+1):
            # Row product
            prod = array[row][col]*array[row][col+1]*array[row][col+2]*array[row][col+3]
            if prod > best:
                best = prod

            # Col product
            prod = array[col][row]*array[col+1][row]*array[col+2][row]*array[col+3][row]
            if prod > best:
                best = prod

    for row in range(n-k+1):
        for col in range(n-k+1):
            #Right diagonal
            prod = array[row][col]*array[row+1][col+1]*array[row+2][col+2]*array[row+3][col+3]
            if prod > best:
                best = prod

    for row in range(n-k+1):
        for col in range(k - 1, n):
            #Left diagonal
            prod = array[row][col]*array[row+1][col-1]*array[row+2][col-2]*array[row+3][col-3]
            if prod > best:
                best = prod

    print best

def largest_product_grid_prob():
    # Create a two dimensional array
    array = [[0 for i in range(20)] for x in range(20)]

    for i in range(0, 20):
        s = str(raw_input())
        array[i] = [int(sp) for sp in s.split()] 

    largest_product_grid(array, 20, 4) # 20 element array, 4 consecutive
 
# PROBLEM 12 (NOT PASSING 2 TESTS)
def divisors(n):
    # If N = a**x * b**y * c**z (a, b, c) are prime. The number of divisors
    # is (a + 1)*(b + 1)*(c + 1)
    if n == 1:
        return 1

    powers = {}
    i = 2
    while n and i <= math.sqrt(n): 
        if n%i == 0:
            n = n/i
            if i in powers:
                powers[i] = powers[i] + 1
            else:
                powers[i] = 1
            i = 2
        else: 
            i = i + 1

    if n > 1:
        if n in powers:
            powers[n] = powers[n] + 1
        else:
            powers[n] = 1

    d = 1
    for i in powers.values():
        d = d * (i + 1)

    return d

def triangle_number(f):
    # Find a triangle number with more than f divisors. Start with 2nd.
    i = 1
    tnum = (i*(i+1))/2
    f1 = divisors(tnum)
    while f1 <= f:
        i = i + 1
        tnum = (i*(i+1))/2
        f1 = divisors(tnum)

    print tnum

def triangle_number_prob():
    get_input1()

    for v in dict.values():
        triangle_number(v)

# PROBLEM 13
def large_sum_prob():
    num_vals = int(raw_input())
    num_digits = 50
    num_print  = 10

    dict = {}
    for i in range(num_vals):
        dict[i] = str(raw_input())

    '''
    # Naive way
    sum = 0
    for v in dict.values():
        sum = sum + int(v)

    print sum
    '''

    s = ""
    carry = 0
    for dec in xrange(num_digits, 0, -1):
        tsum = carry 
        for num in range(num_vals):
            tsum = tsum + int(dict[num][dec-1:dec])
        # Save the number in j-1:j position and carry
        carry = tsum/10
        s = chr(tsum%10+ord('0')) + s

    s = str(carry) + s
    print s[:num_print] 

collatz = {}
# PROBLEM 14 (NOT PASSING A FEW TESTCASES)
def collatz_seq(n):
    global collatz

    c = n

    # Collatz starting at N
    if n in collatz:
        #print "Returning memoized ", n
        return collatz[n]

    seq = 1
    while n != 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1

        if n in collatz:
            #print "Adding memoization and returning ", c, n
            collatz[c] = seq + collatz[n]
            return seq + collatz[n]
            
        seq = seq + 1

    #print "Adding ", c
    collatz[c] = seq

    return seq
        
def longest_collatz_seq(n):
    m = [0, 0]
    l = []
    for i in range(1, n):
        c = collatz_seq(i)
        if c > m[1]:
            m[0] = i
            m[1] = c
            l = []
            l.append(i)
        if c == m[1]:
            l.append(i)

    print max(l)

def longest_collatz_seq_prob():
    get_input1()

    for v in dict.values():
        longest_collatz_seq(v)

# PROBLEM 15 
def lattice_path_combinatrics(n, m):
    # Answer is (N+M) Choose M or N. Since, there will be N DOWN's and M RIGHT's
    return factorial(n+m)/(factorial(m)*factorial(n))

def lattice_path(n, m):
    lattice = [[0 for x in range(m+1)] for y in range(n+1)]

    # Intialize base the right and bottom vertices have 
    # exactly 1 way to get to n,n.
    for i in range(n): # Right
        lattice[i][m] = 1
    for i in range(m): # Bottom
        lattice[n][i] = 1

    for row in xrange(n-1, -1, -1):
        for col in xrange(m-1, -1, -1):
            lattice[row][col] = lattice[row][col+1] + lattice[row+1][col]

    return lattice[0][0]

def lattice_path_rec(n, m, down, right):
    # Find paths in a NxM lattice.
    if right == m and down == n:
        return 1
    
    nr = 0

    if down < n:
        nr = nr + lattice_path_rec(n, m, down+1, right)
    if right < m:
        nr = nr + lattice_path_rec(n, m, down, right+1)

    return nr

def lattice_path_prob():
    num_vals = int(raw_input())

    i = 0
    for i in range(0, num_vals):
        dict[i] = str(raw_input())

    for v in dict.values():
        n, m = v.split()
        #print lattice_path_rec(int(n), int(m), 0, 0)
        #print lattice_path(int(n), int(m))
        print lattice_path_combinatrics(int(n), int(m))

# PROBLEM 16
def power_digit_sum(n):
    num = list(str(2**n))
    print sum([int(i) for i in num])

def power_digit_sum_prob():
    get_input1()

    for v in dict.values():
        power_digit_sum(v)

# PROBLEM 17
digits = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
             7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 
             12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
             19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
             60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

def print_hundred(n):
    if n/100:
        print digits[n/100], "Hundred",

    if not n%100:
        return

    if n%100 < 20:
        print digits[n%100],
    else:
        print digits[((n%100)/10)*10],
        if n%10:
            print digits[n%10],

def print_value(k):
    if k == 4:
        print "Trillion",
    if k == 3:
        print "Billion",
    if k == 2:
        print "Million",
    if k == 1:
        print "Thousand",

def num_to_word(n):
    l = []

    # Split the word and start from the left
    while n:
        l.append(n%1000)
        n = n/1000
   
    for i in xrange(len(l)-1, -1, -1):
        print_hundred(l.pop(i))
        print_value(len(l))

    print

def num_to_word_prob():
    get_input1()

    for v in dict.values():
        num_to_word(v)

# PROBLEM 18
def max_path_sum_triangle(n):
    v, s = dict[n]

    l = [int(c) for c in s.split()]
    m = list(l)

    for i in xrange(v, 1, -1):
        # Start last row
        cur     = (i*(i-1))/2
        cur_end = (i*(i+1))/2
        # Start current row - 1
        prev    = ((i-1)*(i-2))/2 
        for j in range(cur, cur_end-1):
            m[prev] = max(m[j], m[j+1]) + l[prev]
            prev = prev + 1

    print m[0]

def max_path_sum_triangle_prob():
    # N test cases
    # T rows
    # Next T rows have elements 1 to T
    numt = int(raw_input())

    for i in range(numt):
        num_rows = int(raw_input())
        s = ""
        for j in range(1, num_rows+1):
            line = str(raw_input())
            s = s + " " + line
        dict[i] = (num_rows, s)

    for i in range(numt):
        max_path_sum_triangle(i)

# PROBLEM 19 (NOT ALL TESTS PASSED)
# START with MON 01/01/1900
week_days     = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'] 
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

'''
Gaussian algorithm to determine day of week
'''
def day_of_week(year, month, day):
    '''
        w = (d+floor(2.6*m-0.2)+y+floor(y/4)+floor(c/4)-2*c) mod 7
                 
        Y = year - 1 for January or February
        Y = year for other months
        d = day (1 to 31)
        m = shifted month (March = 1, February = 12)
        y = last two digits of Y
        c = first two digits of Y
        w = day of week (Sunday = 0, Saturday = 6)
    '''

    d = day
    m = (month - 3) % 12 + 1
    if m > 10: 
        Y = year - 1
    else: 
        Y = year
    y = Y % 100
    c = (Y - (Y % 100)) / 100
                                 
    w = (d + floor(2.6 * m - 0.2) + y + floor(y/4) + floor(c/4) - 2*c) % 7
                                     
    return int(w)

def leap_year(y):
    return y%4 == 0 and y%400 == 0

def count_days(y, m, d):
    leap_yrs = (y - 1900)/4 + (y - 1900)/400
    centuries = (y - 1900)/100 

    # Add as many days as leap years (4 and 400).
    days = (y - 1900)*365 + leap_yrs - centuries

    # Count months so far and add days
    for i in range(1, m):
        if i == 2 and leap_year(y):
            days = days + leap_days_in_month[i]
        else:
            days = days + days_in_month[i]
    days = days + d

    return days

def counting_sundays_iter(y1, m1, d1, y2, m2, d2):
    count = 0
    for y in range(y1, y2+1):
        # For the last year count till m2
        if y == y2:
            mmax = m2+1
        else:
            mmax = 13
        for m in range(m1, mmax):
            # Include the start and end dates in the range
            # only consider them if day is 1st
            if (y == y1 and m == m1):
                if d1 != 1:
                    continue
            if (y == y2 and m == m2):
                if d2 != 1:
                    continue
            '''
            d = count_days(y, m, 1)
            if d%7 == 0:
            '''
            if day_of_week(y, m, 1) == 0:
                count = count + 1

    print count

def counting_sundays(n):
    y1, m1, d1 = [int(c) for c in dict[n][1].split()]
    y2, m2, d2 = [int(c) for c in dict[n][2].split()]
    counting_sundays_iter(y1, m1, d1, y2, m2, d2)

def counting_sundays_prob():
    numt = int(raw_input())

    for i in range(numt):
        l1 = str(raw_input())
        l2 = str(raw_input())
        dict[i] = (i, l1, l2)

    for i in range(numt):
        counting_sundays(i)

# PROBLEM 20 
def factorial_sum(n):
    l = [int(c) for c in str(math.factorial(n))]
    print sum(l)

def factorial_sum_prob():
    get_input1()

    for v in dict.values():
        factorial_sum(v)

if __name__ == "__main__":
    factorial_sum_prob()

    '''
    counting_sundays_prob()

    max_path_sum_triangle_prob()

    num_to_word_prob()

    power_digit_sum_prob()

    lattice_path_prob()

    longest_collatz_seq_prob()

    large_sum_prob()

    triangle_number_prob()

    largest_product_grid_prob()

    sum_of_primes_prob()

    pythagorean_triplet_prob()

    largest_product_prob()

    nth_prime_prob()

    sum_of_squares_prob()

    smallest_multiple_prob()

    palindrome_prod_prob()

    prime_factor_prob()

    even_sum()

    sum_multiples35()
    '''
