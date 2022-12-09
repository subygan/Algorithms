test_cases = int(input())

for _ in range(test_cases):

    count = int(input())
    even, odd = 0,0
    for value in map(int,input().split(' ')):
        if value % 2 == 0:
            even += 1
        else:
            odd += 1

    if odd % 2 == 1:
        print("YES")
    elif odd > 0 and odd % 2 == 0 and even > 0:
        print("YES")
    else:
        print("NO")