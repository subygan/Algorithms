'''
https://www.hackerrank.com/challenges/repeated-string/
'''


def repeatedString(s, n):
    my_count = s.count('a')
    quo = n//len(s)
    r = s[:n%len(s)].count('a')
    return quo*my_count + r


if __name__ == '__main__':

    print(repeatedString('abcd',100000))
