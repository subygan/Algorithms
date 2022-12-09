# Python3 implementation of Finding
# Length of Longest Common Substring

# Returns length of longest common
# substring of X[0..m-1] and Y[0..n-1]
from icecream import ic


def LCSubStr(X, Y, m, n):
    ic(X,Y,m,n)
    # Create a table to store lengths of
    # longest common suffixes of substrings.
    # Note that LCSuff[i][j] contains the
    # length of longest common suffix of
    # X[0...i-1] and Y[0...j-1]. The first
    # row and first column entries have no
    # logical meaning, they are used only
    # for simplicity of the program.

    # LCSuff is the table with zero
    # value initially in each cell
    LCSuff = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # To store the length of
    # longest common substring
    result = 0

    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                ic(i,j)
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                ic(X[i-1],X[j-1])
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
            ic(LCSuff)

    return result


# Driver Code
X = 'Geeks'
Y = 'GeeksQuiz'

m = len(X)
n = len(Y)

print('Length of Longest Common Substring is',
      LCSubStr(X, Y, m, n))

# This code is contributed by Soumen Ghosh
