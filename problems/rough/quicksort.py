from icecream import ic


def quick_sort(array):
    ic(array)
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop()
        left = []
        right = []
        for i in range(len(array)):
            if array[i] < pivot:
                left.append(array[i])

            else:
                right.append(array[i])
    ic(array, left, right)
    return quick_sort(left) + [pivot] + quick_sort(right)


def k(arr):
    arr+['1']
