'''
https://leetcode.com/problems/zigzag-conversion/
'''

def zig( s: str, r: int) :

    myl = [[] for _ in range(0, r)]
    ans = ''
    l, my_local = 0, 0

    while l < len(s):
        print('<<<======>>>')
        print(l)
        print(myl)
        if my_local < r :
            print(s[l])
            myl[my_local].append(s[l])
            print(myl)
            l += 1
            my_local += 1

        elif my_local < 2*r-2:
            myl[-1*(my_local - r + 2)].append(s[l])
            l += 1
            my_local += 1

        else :
            my_local = 0
    return myl

ans = ''
for i in zig('PAYPALISHIRING',4) :

    ans += ''.join(i)

print(ans)

