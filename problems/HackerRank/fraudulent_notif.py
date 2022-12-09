def get_limit(f,d):
    count = 0
    m1,m2 = (d//2,d//2+1)
    m = []
    for i,j in enumerate(f):
        count+=j
        if not m and m1<=count:
            m.append(i)
        if m2<=count:
            m.append(i)
            break
    return m[-1]*2 if d%2 else sum(m)


def activityNotifications(e, d):
    f = [0]*201
    count = 0
    for i in e[:d]:
        f[i]+=1
    for i,v in enumerate(e[d:]):
        limit = get_limit(f,d)
        if v>=limit:
            count+=1
        f[v]+=1
        f[e[i]]-=1


    return count


with open('/Users/suriyaganesh/Documents/VL/Problems/HackerRank/fraudulent_notif.txt','r') as f:
    n, d = list(map(int, f.readline().split()))
    expenditure = list(map(int, f.readline().split()))

with open('/Users/suriyaganesh/Documents/VL/Problems/HackerRank/fraudulent_notif_out.txt', 'w') as fd:

    result = activityNotifications(expenditure, d)
    print(result)

