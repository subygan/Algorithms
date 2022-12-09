'''
https://codeforces.com/contest/1521/status/A
'''

for _ in [0]*int(input()):
    A, B = map(int,input().split())
    if B!=1:
        print("YES")
        print(A,A*B,A*(B+1))
    else:
        print("NO")