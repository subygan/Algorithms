from icecream import  ic
from collections import  defaultdict


class Solution:
    def traverse(self, gr, path, n, i):
        print('<<<---------- traverse --------------->>>')
        ic(gr, path, n, i)

        if len(path) == n:
            return 1

        x = 0
        for j in gr[i]:
            if j not in path:
                path.append(j)
                if len(path) == n:
                    return 1
                x = self.traverse(gr, path, n, j)
                path = path[:-1]
        return x

    def check(self, N, M, Edges):
        gr = {}
        for z in range(1,N+1): gr[z]=[]

        print(gr)

        if M < N - 1:
            return 0

        for i in Edges:
            gr[i[0]].append(i[1])

        x =0
        for z in range(1,N+1):

            print(f'\n\n<<<----------- for {z}    ---->>>\n\n')

            x = self.traverse(gr,[z], N, z)
            ic(x, z)
            if x == 1:

                return x

        return x

if __name__ == '__main__':

    for _ in range(int(input())):
        n,m = list(map(int,input().split()))

        e = list(map(int, input().strip().split()))
        edges = []

        for i in range(m):
            edges.append([e[2*i],e[2*i+1]])


        ob = Solution()
        if ob.check(n,m,edges): print(1)
        else: print(0)
    z = defaultdict()

    # edge = [[1,2],[2,3],[5,4],[2,4]]
    #
    # print(check(5,len(edge), edge))
# 10 14
# 2 1 10 2 6 3 5 4 10 5 10 6 6 7 6 8 10 9 4 9 3 8 3 7 5 9 6 5