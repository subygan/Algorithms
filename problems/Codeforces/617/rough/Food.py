test_cases = int(input())

for _ in range(test_cases):

    value = input()

    new_ones = 0
    total = int(value)

    for _ in range(len(value)):
        new_ones = int(value)//10
        total += new_ones
        value = new_ones + int(value)%10

    print(total)