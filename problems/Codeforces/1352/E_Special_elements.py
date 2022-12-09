# for s in [*open(0)][2::2]:
for _ in range(int(input())) :
    value = int(input())
    s = input()
    a = *map(int, s.split()),
    print(a)
    n = len(a)
    b = 2 * n * [0]
    r = 0
    for x in a: b[x] += 1
    for i in range(n):
        t = a[i]
        # print('b for :', b)
        # print('t for :', t)
        while i + 1 < n >= t + a[i + 1]:
            # print('i, t, r, b before :', i, t, r, b)
            i += 1
            t += a[i]
            r += b[t]
            b[t] = 0
    #         print('i, t, r, b after  :',i, t, r, b,'\n')
    #     print('<<<=== End While ===>>>')
    # print('<<<=== End For ===>>>')
    print(r)

'''
url : https://codeforces.com/contest/1352/problem/E
'''