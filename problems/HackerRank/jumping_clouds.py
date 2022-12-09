'''
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
'''

def jumpingOnClouds(c):
    x,y = 0,0
    while x<len(c)-2:
        x = x+1 if c[x+2] else x+2
        y+=1
    if x<len(c)-1:
        y+=1
    return y


if __name__ == '__main__':

    print(jumpingOnClouds(list(map(int, '0 0 1 0 0 1 0'.rstrip().split()))))