def fib(n):
    v1, v2, v3 = 3, 1, 0    # initialise a matrix [[1,1],[1,0]]

    print(bin(n)[2:])
    print(bin(n))
    for rec in bin(n)[2:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        print(rec)
        print(v1,v2,v3)
        calc = v2*v2
        # v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        v1 = v1^2
        print(v1)
        if rec=='1':   v1*=v1
        # print(v1,v2,v3)
        print("<<<======>>>")
    return v1


print(fib(12))
