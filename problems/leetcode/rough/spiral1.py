matrix = [[1,2,3,4],[4,5,6,12],[7,8,9,11]]

def spiral(matrix):
    ans = []
    x = len(matrix)//2
    y = len(matrix[0])//2
    for i in range(min(len(matrix)//2,len(matrix[0])//2)+1):
        if x == len(matrix)/2 and i == min(len(matrix)//2,len(matrix[0])//2):
            n = 2
        elif y == len(matrix[0])/2 and i == min(len(matrix)//2,len(matrix[0])//2):
            n = 1
        else:
            n = 4
        for j in range(n):
            if j == 0:
                for y in [matrix[i][x] for x in range(i,len(matrix[0])-i)]:
                    ans.append(y)
            elif j == 1:
                for y in [matrix[x][len(matrix[0])-i-1] for x in range(i+1,len(matrix)-i)]:
                    ans.append(y)
            elif j == 2:
                for y in [matrix[len(matrix)-i-1][x] for x in range(len(matrix[0])-i-2,i-1,-1)]:
                    ans.append(y)
            else:
                for y in [matrix[x][i] for x in range(len(matrix)-i-2,i,-1)]:
                    ans.append(y)
    flatten = []
    return ans

print(spiral(matrix))

