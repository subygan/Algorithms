def init_sting(zeros, switches, ones):
    if zeros:
        current_sting = '0' * (zeros + 1)
        zeros = 0
    elif ones:
        current_sting = '1' * (ones + 1)
        ones = 0
    else:
        current_sting = '01'
        switches -= 1
    return current_sting, zeros, switches, ones


def solve(current_sting, zeros, switches, ones):
    if not current_sting:
        current_sting = solve(*init_sting(zeros, switches, ones))

    elif zeros:
        current_sting += '0' * (zeros + 1)
        zeros = 0
        switches -= 1
        current_sting = solve(current_sting, zeros, switches, ones)

    elif ones:
        current_sting += '1' * (ones + 1)
        ones = 0
        switches -= 1
        current_sting = solve(current_sting, zeros, switches, ones)

    elif switches:
        current_sting += '1' == current_sting[-1] and '0' or '1'
        switches -= 1
        current_sting = solve(current_sting, zeros, switches, ones)

    return current_sting


n = int(input())
inputs = []
for i in range(0, n):
    new_line = [int(x) for x in input().split(' ')]
    inputs.append(new_line)

for i in range(0, n):
    new_line = inputs[i]
    print(solve('', new_line[0], new_line[1], new_line[2]))