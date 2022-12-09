''''
123456789101112131415161718192021…..
you should compute the nth element in this pattern. for example the 11th element is 0 the 15th element is 2.
'''
from icecream import ic


def fun(n):
    prev=0
    tot=9
    t = 1
    while tot<n:
        prev = tot
        tot+=9*(10**t)*(t+1)
        t+=1

    r = n-prev
    if r%t > 0:
        pos = (10**(t-1)) + (r//t)+1
    else:
        pos = (10**(t-1)) + (r//t)

    ic(n,r,tot,prev,t,pos)

    # which = t - n%t
    # ic(which)
    #
    # for i in range(n%t):
    #     print(pos%10**(i+1))


fun(24)

1234567891011121314151617