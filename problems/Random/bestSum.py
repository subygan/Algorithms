def bestSum(target, numbers):
    ds = [None for _ in range(target)]

    for i,v in enumerate(ds):
        if ds[i]!=None:
            for number in numbers:
                ds[i+number] = [*ds[i], number]





arr = [5,3,4,7]
print(bestSum(7,arr))