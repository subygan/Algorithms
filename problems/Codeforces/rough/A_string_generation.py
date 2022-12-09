for _ in range(int(input())):

    n,k = list(map(int, input().split()))
    x = ['a','b','c']
    pal = 'a'*k
    np = 'abc'*(n//3)+ 'abc'[:n%3]
    print((np[:-1*k] if np[-k]!='a' else np[:-k-1]+'b') +pal)
