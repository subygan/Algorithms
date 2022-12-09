number = int(input())

values = [*map(int,input().split(" "))]

index = values.index(max(values))

temp = values[index]
values[index] = values[0]
values[0] = temp

print(*values)