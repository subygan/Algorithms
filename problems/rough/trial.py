AB = []
for _ in range(int(input())):
    [n, m, kma] = [*map(int, input().split(" "))]
    A = [*map(int, input().split(" "))]
    B = [*map(int, input().split(" "))]
    count = 0
    temp = 0
    print(kma)
    for a in range(n-1):
        print("<<<====>>>")
        print("temp :", temp)
        for b in range(temp, m-1):
            if B[b] < A[a]:
                AB.append(B[b])
            else:
                AB.append(A[a])
                temp = count
                break
            print(count)
            if count == kma:
                print(AB[count])
            else:
                count += 1

    print(*AB)