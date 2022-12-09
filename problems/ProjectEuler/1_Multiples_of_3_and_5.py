'''
https://projecteuler.net/problem=1
'''

threes  = 3*(sum([i for i in range(1,334)]))
fives  = 5*(sum([i for i in range(1,200)]))
fifteens = 15*(sum([i for i in range(1,67)]))

print(sum([i for i in range(1,334)]))

print(threes+fives-fifteens)