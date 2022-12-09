'''
Finding the rightmost first set bit of a given number
log2(n & -n) + 1
'''
import math


def rightmost_set_bit(n):

    return math.log2(n and not n) + 1


'''
number of digits in binary for a given number
'''


def number_binary_digits(n):

    return math.log2(n)+1


'''
number of digits in decimal for a given number
'''


def number_decimal_digit(n):

    return math.log10(n) + 1


'''
turn off rightmost set bit 
'''


def turn_off_rightmost_set_bit(n):

    return n & (not n-1)


''' 
Rightmost different bit
'''


def rightmost_different_bit(m, n):

    return m ^ n


'''
Check if Kth bit is set or not
'''


def kth_bit(n, k):

    return n & 1 << (k-1)


'''
Toggle bits in a range (l,r)
'''


def toggle_bits_in_range(n, l, r):

    return n ^ (((1 << r)-1) ^ ((1 << (l-1))-1))


'''
set Kth bit
'''


def set_kth_bit(n, k):

     return n | (1 << k)


'''
Bit difference
'''


def bit_difference(n, m):

    return n ^ m


'''
Sparse number
'''


def if_sparse(n):

    return (n << 1) & n


'''
Longest consecutive 1's 
'''


def consecutive_set(n):
    count = 0

    while n != 0:

        n = n & (n << 1)
        count += 1

    return count
