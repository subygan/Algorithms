
# Implement your solution by completing the below function
def numIslands(grid):
    x = 0
    names = 0
    ans = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                names += 1
                grid = replacevals("v",grid,i,j)
                print("\n")
                for row in grid:
                    for value in row:
                        print(value,end="")
                    print()
                print("\n\n")
            else:
                continue
    return names
    # for i in grid:
    #     ans += i
    # if 0 in ans:
    #     return len(set(ans))-1
    # else:
    #     return len(set(ans))

def replacevals(a,matrix,m,n):
    matrix[m][n] = a
    if m+1 < len(matrix) and matrix[m+1][n] == 1:
        # print(matrix)
        matrix = replacevals(a,matrix,m+1,n)
    if m-1 >= 0 and matrix[m-1][n] == 1:
        # print(matrix)
        matrix = replacevals(a, matrix, m - 1, n)
    if n+1 < len(matrix[0]) and matrix[m][n+1] == 1:
        # print(matrix)
        matrix = replacevals(a, matrix, m, n + 1)
    if n-1 >= 0 and matrix[m][n-1] == 1:
        # print(matrix)
        matrix = replacevals(a, matrix, m, n - 1)
    # print(matrix)
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
