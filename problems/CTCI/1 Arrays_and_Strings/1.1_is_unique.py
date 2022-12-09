def using_arr(arr) :
    my_arr = []

    for element in arr :
        if arr not in my_arr:
            my_arr.append(element)
        else :
            return False
    return True


def using_dict(arr) :

    my_dict = {}

    for element in arr :

        if arr not in my_dict :
            my_dict[element] = 1
        else :
            return False
    return True


if __name__ == "__main__" :
    arr = input().split(' ')
    print(f'using an array O(n\u00b22) : {using_arr(arr)}')
    print(f'using an array O(n) : {using_dict(arr)}')

    print()

'''
Implementing and algorithm to determine if a string has all unique characters. What if you cannot use additional characters
'''