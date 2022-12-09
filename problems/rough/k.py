



l = [1,2,3,4,5,6,7,8,9]
l.sort(reverse=True)
prev = 0
for k in range(0,len(l),3 ):
    print(k)
    print(l[prev:k])

print(l[prev:])