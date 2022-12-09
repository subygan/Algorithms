# from icecream import ic


def isInterleaved(A, B, C):
    res = []
    l = len(A)+len(B)
    # ic(A,B,C,res)
    k = True
    ca, cb = 0, 0
    for i in range(l):
        # ic(i,res,ca)

        if k:
            if ca < len(A):
                res.append(A[ca])
                ca += 1
                k=False
            else:
                res.extend(B[cb:])
                break
        elif not k:
            if cb < len(B):
                res.append(B[cb])
                cb += 1
                k = True
            else:
                res.extend(A[ca:])
                break

    # ic(A,B,C,res)
    # print('\n\n<<<===========>>>\n\n')
    return 1 if ''.join(res) == C else 0


def test(A, B, C):
    if (isInterleaved(A, B, C) or isInterleaved(B,A,C)):
        print(C, "is interleaved of", A, "and", B)

    else:
        print(C, "is not interleaved of", A, "and", B)

if __name__ == '__main__':
    test("XXY", "XXZ", "XXZXXXY")
    test("XY", "WZ", "WZXY")
    test("XY", "X", "XXY")
    test("YX", "X", "XXY")
    test("XXY", "XXZ", "XXXXZY")