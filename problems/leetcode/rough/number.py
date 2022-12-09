grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
r = len(grid)
c = len(grid[0])

normalised = k % (r*c)
my_list = [j for i in grid for j in i]
new_list = []

