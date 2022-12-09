from icecream import ic


def quick_sort(array):
    k = 0
    if [1,2] == array:
        k = 1

    if len(array) <= 1:
        return array
    else:
        pivot = len(array) // 2
        left = []
        right = []
        if k: ic(pivot,left, right)
        for i in range(len(array)):
            if array[i] <= array[pivot]:
                left.append(array[i])
            else:
                right.append(array[i])

    quick_sort(left) + [array[pivot]] + quick_sort(right)


a = [1, 2, 3, 7, 5, 8, 31, 11, 12]
quick_sort(a)
print(a)