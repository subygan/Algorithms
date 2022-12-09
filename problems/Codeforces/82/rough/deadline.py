import math

test_cases = int(input())

for _ in range(test_cases):

    n,d = map(int,input().split(" "))

    if d <= n :

        print("YES")

    else:

        for trials in range(n) :

            if (trials + math.ceil((d / (trials + 1)))) <= n:
                print("YES")
                break
        else:
            print("NO")
