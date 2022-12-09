for _ in range(int(input())):

    value = int(input())
    count = 0

    while value > 0:

        if value & 1 :

            count += 1
            value -= 1
        else:
            value = value//2
            count += 1

        print(value)

    print(count)
