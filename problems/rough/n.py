from icecream import ic
b = [1,2,3,4,5]


height = b + [0]
s = []
_sum = 0
i = 0

while i < len(height):
    ic('--------while--------')
    ic(i,s,_sum)
    if not s or height[i] > height[s[-1]]:
        print('\t----------if---------')
        s.append(i)
        i+=1
    else:
        print('\t----------else---------')
        t = s[-1]
        s = s[:-1]
        _sum = max(_sum, height[t]*(i if not s else (i - s[-1] - 1)))
        ic(_sum)

print(_sum)
