def sort_to_find(A,B) :
    sorted_a = A.sort()
    sorted_b = B.sort()

    for pos in range(len(sorted_a)) :

        if sorted_a[pos] != sorted_b :
            return False
    return True


def letter_count(A, B):

    my_dict = {}

    for letter_a in A:

        try :
            my_dict[letter_a] += 1
        except KeyError:
            my_dict[letter_a] = 1

    for letter_b in B:

        try :
            if my_dict[letter_b] > 1 :
                my_dict[letter_b] -= 1
            else :
                del my_dict[letter_b]
        except KeyError:
            return False

    if my_dict:
        return False
    else:
        return True

if __name__ == "__main__" :

    A = list(input())
    B = list(input())

    print(letter_count(A, B))


'''
Given two strings, write a method to figure out if one is a permutation of the other
'''