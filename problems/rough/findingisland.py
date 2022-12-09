
# Implement your solution by completing the below function
def numIslands(grid):
    x = 0
    names = 3
    ans = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                names += 1
                grid = replacevals(names,grid,i,j)
                # print("\n")
                # for row in grid:
                #     for value in row:
                #         print(value, end="")
                #     print()
                # print("\n\n")
            else:
                continue
    for i in grid:
        ans += i
    if 0 in ans:
        return len(set(ans))-1
    else:
        return len(set(ans))

def replacevals(a,matrix,m,n):

    matrix[m][n] = a

    # looking up
    if m+1 < len(matrix) and matrix[m+1][n] == 1:
        # print("<<== looking down ===>>")
        matrix = replacevals(a,matrix,m+1,n)

    # looking down
    if m-1 > len(matrix) and matrix[m-1][n] == 1:
        # print("<<== looking up ===>>")

        matrix = replacevals(a, matrix, m - 1, n)

    # looking right
    if n+1 < len(matrix[0]) and matrix[m][n+1] == 1:
        # print("<<== looking right ===>>")
        matrix = replacevals(a, matrix, m, n + 1)

    # looking left
    if n-1 >= 0 and matrix[m][n-1] == 1:
        # print("<<== looking left ===>>")
        matrix = replacevals(a, matrix, m, n - 1)

    return matrix

if __name__ == '__main__':
    row = input().split()
    n = int(row[0])
    m = int(row[1])
    grid = []
    for i in range(n):
        r = list(map(int,input().split()))
        grid.append(r)
    result = numIslands(grid)
    print(result)

'''
5 5
0 0 1 0 0
0 1 1 1 0
1 1 1 1 1
0 0 1 0 0
0 0 1 0 0
'''
