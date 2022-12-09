"""
https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""

n,k = map(int, input().split())
numbers = map(int, input().split())

count = [0]*k

for number in numbers:
    count[number%k] += 1

total = min(count[0],1)

for i in range(1, k//2+1):
    if i != k-i:
        total +=max(count[i], count[k-i])

    else:
        total+=min(count[i],1)

print(total)