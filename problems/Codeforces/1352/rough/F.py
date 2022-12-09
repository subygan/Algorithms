for _ in range(int(input())):

    data = *map(int,input().split()),
    n0, n1, n2 = data[0], data[1], data[2]
    my_string = ''

    if n1 == 0 :
        if n0 > 0 and n2 ==0 :
            my_string = '0'*(n0+1)
        elif n2 != 0 :
            my_string = '1'*(n2+1)
        else :
            my_string = ''

    else :
        mystring_n1 = '10'*(n1//2 + n1%2)
        if not n1%2 :
            mystring_n1+='1'
        if n0 >0:
            mystring_n1 = mystring_n1[0] + '0'*n0 + mystring_n1[1:]
        if n2 >0:
            mystring_n1 = '1'*n2+mystring_n1
        my_string = mystring_n1
    print(my_string)




