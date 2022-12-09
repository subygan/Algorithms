def collectOne(n,coordinate):
    coordinate.sort(key=lambda x:x[1])
    coordinate.sort(key=lambda x:x[0])
    #print(coordinate)
    for i in range(len(coordinate)-1):
        if coordinate[i][1] > coordinate[i+1][1]:
            return "NO"
    path = list()
    coordinate.insert(0,[0,0])
    for i in range(len(coordinate)-1):
        path.append("R"*(coordinate[i+1][0]-coordinate[i][0]))
        path.append("U"*(coordinate[i+1][1]-coordinate[i][1]))
    return "YES\n"+"".join(path)
def main():
    t = int(input())
    outcome = list()
    for i in range(t):
        n = int(input())
        coordinate = [list(map(int,input().split())) for _ in range(n)]
        outcome.append(collectOne(n,coordinate))
    print("\n".join(outcome))
main()