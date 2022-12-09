'''

https://www.hackerrank.com/challenges/counting-valleys/problem

'''


def countingValleys(n, s):
    position = 0
    peak = 0
    for i in range(n):
        if s[i] == 'U':
            position += 1
        elif s[i] == 'D':
            position -= 1
        if position == 0 and s[i] == 'U':
            peak += 1
    return peak


if __name__ == "__main__":
    print(countingValleys(8, 'UDDDUDUU'))
