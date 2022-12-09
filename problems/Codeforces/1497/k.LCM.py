# https://codeforces.com/contest/1497/problem/C1

for _ in range(int(input())):
    n,k = map(int,input().split())
    if n%4==0:
        print(n//2,n//4,n//4)
    elif n%2==0:
        print((n//2)-1,(n//2)-1,2)
    else:
        print(n//2,n//2,1)
