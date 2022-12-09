def maxSubArraySum(arr, l, h):
    if (l == h):
        print("!!!!!!!!!")
        print(arr)
        print(arr[l])
        print("------------")
        return arr[l]

    m = (l + h) // 2

    print("maxSubArraySum")

    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m + 1, h),
               maxCrossingSum(arr, l, m, h))


'''
max crossing sum, to find the crossing sum in a value.
there are two loops, one starting from mid to left end, other starting from mid+1 to right end
max sum is calculated from both and result is calculated.
'''


def maxCrossingSum(arr, l, m, h):
    sm = 0
    left_sum = -1000000
    for i in range(m, l - 1, -1):
        sm = sm + arr[i]
        if sm > left_sum:
            left_sum = sm
    sm = 0
    right_sum = -10000000
    for i in range(m + 1, h + 1):

        sm = sm + arr[i]
        if sm > right_sum:
            right_sum = sm
    print(left_sum, right_sum)

    return left_sum + right_sum


arr = [-2, -3, 4, -1, -2, 1, 5, -3]

n = len(arr)

maximum = maxSubArraySum(arr, 0, n - 1)

print(maximum)
