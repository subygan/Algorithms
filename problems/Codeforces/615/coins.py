test_cases = int(input())

for _ in range(test_cases):

    A,B,C,n = map(int,input().split(" "))

    total = sum([A,B,C,n])

    if total%3 >0:
        print("NO")
        continue
    else:
        average = total/3

        if A>average or B>average or C>average:
            print("NO")
            continue
        else:
            print("YES")
            continue