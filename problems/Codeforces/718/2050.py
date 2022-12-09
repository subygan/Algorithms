'''
https://codeforces.com/problemset/problem/1517/A
'''

for i in range(int(input())):
    n=int(input())
    print(-1 if n%2050 else sum(map(int,str(n//2050))))
