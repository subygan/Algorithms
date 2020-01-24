'''
A naive solution using for loop to find the solution
runs at O(n).
not very efficient, could be improved.
'''


def exp(num, pow):

    value = 1
    for i in range(0,pow):
        value *= num

    return value


'''
Fast exponentiation, using exponentiation by doubling
the idea, is to break down the number to its bits and exponentially double.
'''


def fast_exp(num,pow):
    value = 1

    print(bin(pow))
    for rec in bin(pow)[2:]:
        value = value**2
        if rec == "1": value *= num
        print(value)
        print("<<<=======>>>")

    return value


if __name__ == '__main__':

    print(fast_exp(2, 10000000))