# this takes linear time to find the max crossing subarray
def max_crossing(lis, low, mid, high):
    left_sum = float('-inf')
    sum, max_left, max_right = 0,0,0
    for i in range(mid, low, -1):
        sum += lis[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i


    right_sum = float('-inf')
    sum = 0
    for i in range(mid+1, high):
        sum += lis[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return (max_left, max_right, left_sum+right_sum)


def max_subarray(lis, low, high):
    if high == low:
        return(low, high, lis[low-1])
    else:
        mid = (low+high)//2
        (left_low, left_high, left_sum) = max_subarray(lis, low, mid)
        print("left",left_low, left_high, left_sum)
        (right_low, right_high, right_sum) = max_subarray(lis, mid+1, high)
        print("right",right_low, right_high, right_sum)
        (cross_low, cross_high, cross_sum) = max_crossing(lis, low, mid, high)
        print("cross",cross_low, cross_high, cross_sum)
    if left_sum >= right_sum and left_sum >= cross_sum: return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum: return (right_low, right_high, right_sum)
    else: return (cross_low, cross_high, cross_sum)

mine = [1,2,2,3]

x = max_subarray(mine, 0, len(mine))
print(x)
print(len(mine))

for i in range (0, len(mine)):
    print(i)