'''
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array
'''

arr = [1,2,3,44,5,5,224,1,1,1,3,3,4]
mini = float('inf')
a = arr.sort()

for i in range(len(arr) - 1):
    mini = min(mini, abs(arr[i] - arr[i+1]))
print(mini)