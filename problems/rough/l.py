from icecream import ic

k = [2,6,1,12]
n = len(k)


def return_min(arr, mins, limits):
    minimum = mins
    ic(limits, mins)
    ic(arr[limits[1]-1])
    if mins and arr[limits[1]-1] < mins[1] :
        minimum = [limits[1]-1, arr[limits[1]-1]]
        ic('*', minimum)

    elif not mins or limits[0]-1 == mins[0]:
        a = arr[limits[0]:limits[1]][0]
        minimum = [limits[0],a]
        ic('!!!!!!!',minimum)
        count = 0
        for i, v in enumerate(arr[limits[0]:limits[1]]):
            ic(i,v)
            if v<a:
                a = v
                minimum = [limits[0]+count,v]
            count += 1
    return minimum


result = []
for i in range(1,n+1):
    print(i)
    limits = [0, n - i + 1]
    mins = []
    cur_min1 = []
    for j in range(i):
        # ic(limits)
        ic(k[limits[0]:limits[1]])
        # cur_min = min(k[limits[0]:limits[1]])
        cur_min1 = return_min(k, cur_min1, limits)
        ic(cur_min1)

        limits = [limits[0]+1,limits[1]+1]
        mins.append(cur_min1[1])

    result.append(max(mins))
ic(result)
