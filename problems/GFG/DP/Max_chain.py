from itertools import izip

t = [1, 243, 4, 42, 42, 4, 5]

pairs = izip(*[iter(t)]*2)

print(pairs)
