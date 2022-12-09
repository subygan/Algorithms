from icecream import ic
l = [1,10,11,1]
s =[l[0]]
for i in l[1:]:
    left = 0
    right = 0
    while i < s[-1]:
        s = s[:-1]
    s.append(i)
    ic(i,s)

