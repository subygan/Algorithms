

def check_index(list, l, r):

    if l+1 == r or l == r :
        return -1

    else:

        if list[l] == list[r] :

            return check_index(list, l+1, r-1)

        else:

            return




