for _ in range(int(input())) :
    [N,M] = input().split(" ")
    Fruits = input().split(" ")
    price = list(map(int,input().split(" ")))
    my_dict = {}
    minimum = [["f",100000000000000000000]]

    for element in range(len(price)) :

        fruit = Fruits[element]

        try:
            my_dict[fruit]
            my_dict[fruit] = my_dict[fruit] + price[element]

        except KeyError:
            my_dict[fruit] = price[element]

        if fruit == minimum[0][0] and my_dict[fruit]>0 :

            minimum[0][1] = my_dict[fruit]

        elif my_dict[fruit] < minimum[0][1] and my_dict[fruit]>0 :

            minimum[0][0] = fruit
            minimum[0][1] = my_dict[fruit]
    print(type(minimum[0][1]),end="")


