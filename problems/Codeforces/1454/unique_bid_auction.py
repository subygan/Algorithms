for _ in range(int(input())):
    n = input()
    bid = list(map(int, input().split()))
    unique = {}
    everything ={}

    for index, value in enumerate(bid):

        if value in everything.keys():
            if value in unique.keys():
                del unique[value]
        else:
            unique[value] = index
        everything[value] = index

    if unique:
        print(unique[min([i for i in unique.keys()])]+1)
    else:
        print(-1)

