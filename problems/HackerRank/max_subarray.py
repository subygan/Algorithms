def algo(arr, start, end):
    odd, even = 0
    for i in range(start, end, 2):
        even += arr[i]
        odd += arr[i + 1]
    return even ** 2 - odd ** 2

