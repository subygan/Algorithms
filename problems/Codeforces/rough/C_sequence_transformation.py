for _ in range(int(input())):
    n = input()
    seq = [*map(int, input().split())]
    a, b = seq[0], seq[-1]

    prev = -1


    for index, el in enumerate(seq):
        if prev == el:
            del seq[index]

    my_dict = {i:seq.count(i) for i in seq}
    value = min(my_dict, key=my_dict.get)


