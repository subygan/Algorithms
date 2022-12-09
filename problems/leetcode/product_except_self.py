"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/827/
"""
my_list = [1, 2, 3, 4]
k = len(my_list)
new_list = [1]*k

for i in range(1,k):
    new_list[i] = new_list[i-1]*my_list[i-1]

r = 1
for i in range(k-1,-1,-1) :
    new_list[i]*=r
    r*=my_list[i]

print(new_list)