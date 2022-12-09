def pos(mat, val, loc):
    m = {
        'W':'R',
        'R':'W',
        '.':'.'
    }
    # print(mat,val,loc)
    around = [
        mat[loc[0]-1][loc[1]] if loc[0]-1 >=0 else m[val],
        mat[loc[0]+1][loc[1]] if loc[0]+1 <len(mat) else m[val],
        mat[loc[0]][loc[1]-1] if loc[1]-1 >=0 else m[val],
        mat[loc[0]][loc[1]+1] if loc[1]+1 <len(mat[0]) else m[val],
    ]
    if val in around: return 0
    else: return 1


def solve(mat,loca,state=False):

    if checkmat(mat):
        print('YES')
        printify(mat)
        return 1
    else:
        for i in range(loca[0],len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == '.':
                    if pos(mat,'R', [i,j]):
                        mat[i][j] = 'R'
                        x = solve(mat, [i,j],state=False)
                        if not x: mat[i][j] = '.'
                        else: return x
                    elif pos(mat,'W',[i,j]):
                        mat[i][j] = 'W'
                        x = solve(mat, [i,j], state=False)
                        if not x :
                            mat[i][j] = '.'
                        else:
                            return x
                    else:
                        return 0

    return 0

def checkmat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if not pos(mat,mat[i][j],[i,j]): return 0

    return 1

def printify(mat):
    for i in mat:
        print(''.join(i))


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        x,y = list(map(int, input().split()))
        mat = []
        for i in range(x):
            mat.append(list(input()))
        x = solve(mat,[0,0])
        if not x: print('NO')



'''
4
4 6
.R....
......
......
.W....
4 4
.R.W
....
....
....
5 1
R
W
R
W
R
5 1
R
R
R
R
R
3 2
..
..
.R
2 2
..
RR
10 10
..........
..........
..........
..........
..........
..........
..........
..........
..........
.........W
'''