def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]

    print(bin(n)[3:])
    print(bin(n))
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        print(rec)
        print(v1,v2,v3)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        print(v1,v2,v3)
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
        print(v1,v2,v3)

        print("<<<======>>>")
    return v2

print(fib(12))