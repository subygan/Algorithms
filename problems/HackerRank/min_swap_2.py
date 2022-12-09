'''
https://www.hackerrank.com/challenges/minimum-swaps-2
'''

def minimumSwaps(arr):

    temp = 0
    swap = 0
    i = 0

    # arr[0], arr[arr[0]-1] = arr[arr[0]-1], arr[0]
    # print(arr)
    # exit()

    while i < len(arr):
        if i+1 != arr[i]:
            temp = arr[i]
            arr[i], arr[temp-1] = arr[temp-1], arr[i]
            swap += 1
        else:
            i += 1
    return swap


if __name__ == '__main__':

    print(minimumSwaps(list(map(int, '2 3 4 1 5'.rstrip().split()))))