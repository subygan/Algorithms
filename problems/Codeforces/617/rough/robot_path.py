test_cases = int(input())


for _ in range(test_cases):

    num = int(input())

    path = input()
    pos = [0,0]
    visited = [[0,0]]
    length = 0
    min = 10000000000000000
    location = [0,0]
    printed = 0

    for move in path:
        print("<<<=====>>>")
        print(move)

        if move == "L":
            pos[0] = pos[0] - 1
        elif move == "R":
            pos[0] = pos[0] + 1
        elif move == "U":
            pos[1] = pos[1] + 1
        elif move == "D":
            pos[1] = pos[1] - 1

        if pos not in visited:
            print("not_visited")
            visited.append(pos)
            print(visited)
        else:
            print(";;;;;;")
            print(pos,visited)
            print("----")
            inde_x = visited.index(pos)
            diff = length - inde_x
            if diff < min:
                if diff <= 2:
                    print("****")
                    print(diff)
                    min = diff
                    location[0] = inde_x
                    location[1] = length
                    printed = 1
                    print(inde_x)
                    print(location[0]+1,location[1]+1)
                    break
                else:
                    min = diff
                    location[0] = inde_x
                    location[1] = length
        length+=1

    if printed == 0 and location != [0,0]:
        print(location[0]+1,location[1]+1)
    elif location == [0,0] and printed == 0:
        print(-1)


