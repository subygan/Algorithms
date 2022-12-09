tests = int(input())

for _ in range(tests):

    A,B = input().split(" ")

    result = int(A)*(len(str(int(B)+1))-1)
    print(result)