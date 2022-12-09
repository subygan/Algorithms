'''
https://www.hackerrank.com/challenges/frequency-queries/problem
'''
from icecream import  ic

def update_freq(freq, fr, do):
    # ic(freq, fr, do)
    if do == 'add':
        freq[fr] = freq.get(fr, 0) + 1
        if fr>=1: freq[fr-1] = freq.get(fr-1,0) - 1
    else:
        freq[fr] = freq.get(fr, 0) + 1
        freq[fr+1] = freq.get(fr+1) - 1

    return freq


def freqQuery(queries):
    freq, data, ans = {}, {}, []
    for query in queries:
        val = query[1]
        if query[0] == 1:
            data[val] = data.get(val, 0) + 1
            freq = update_freq(freq, data[val], 'add')
        elif query[0] == 2:
            if val in data and data[val]!=0:
                data[val] = data.get(val, 1) - 1
                freq = update_freq(freq, data[val],'sub')

        else:
            if val in freq and freq[val] > 0:
                ans.append(1)
            else:
                ans.append(0)
    print('data', data)
    return ans


with open("./HackerRank/freq_query/input08.txt") as fp:
    Lines = fp.readlines()
    arr = []
    count = 0
    for line in Lines:
       arr.append(list(map(int, line.rstrip().split())))
       if arr[-1][0] == 3:
           count += 1
       if count == 998:
           ic(arr[-3:])
           count+=1
    ans = freqQuery(arr[1:])

with open("./HackerRank/freq_query/my_output.txt", "w") as f:
    # Writing data to a file
    count = 0
    for i in ans:
        f.write(str(i)+'\n')
    print()
    r = 1


