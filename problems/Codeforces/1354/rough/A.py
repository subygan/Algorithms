for _ in range(int(input())):

    a, b, c, d = list(map(int, input().split()))

    if d >= c or a == 0:

        if b >= a:
            if b>0:
                print(b)
            else:
                print(-1)
        else:
            print(-1)

    else:
        effective_sleep = c - d
        remainder_sleep = a - b
        # if remainder_sleep !=0:
        #     if effective_sleep != 0 :
        number_of_cycles = remainder_sleep // effective_sleep
        if remainder_sleep % effective_sleep:
            number_of_cycles += 1

        print(b + number_of_cycles * c)




