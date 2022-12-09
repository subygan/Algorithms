for _ in range(int(input())) :

    my_list = []
    value = int(input())
    number = value
    count = 0

    for i in range(number):

        if number == 0:
            break
        remainder = number % 10
        number = number//10
        if remainder != 0:
            my_list.append(remainder*(10**count))

        count += 1
    print(len(my_list))
    print(*my_list)
