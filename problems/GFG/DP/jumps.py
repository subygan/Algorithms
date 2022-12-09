for _ in range(int(input())):
    value = [1, 2, 3, 5, 9, 1, 2, 4, 5, 3, 2, 1, 4, 5]
    positions = int(input())
    values = [map(int, input().split(" "))]

    print(0, value[0], value)
    for i in value:

        try:
            value = value[value[i]:]
        except IndexError:
            print("done")
            break

        print(i, value[i], value)
