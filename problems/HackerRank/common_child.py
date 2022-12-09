from icecream import ic
def LCS(s1, s2):
    n, m = len(s1), len(s2)
    lcs = [[0] * (m + 1) for _ in range(n + 1)]
    ic(lcs)
    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            ic(i,c1,j,c2)
            if c1 == c2:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
            ic(lcs)
    return lcs[n - 1][m - 1]


if __name__ == '__main__':
    a = input()
    b = input()

    print(LCS(a, b))