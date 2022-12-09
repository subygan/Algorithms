'''
https://codeforces.com/contest/1287/problem/B
'''
from itertools import combinations

def calc_diff(value1,value2):
    my_list = ["S","E","T"]
    string = ""
    for i in range(len(value1)):
        if value1[i] == value2[i]:
            string+=value2[i]
        elif value1[i]!=value2[i]:
            temp = [value1[i],value2[i]]
            string += [i for i in my_list if i not in temp][0]

    return string


cards,features = map(int,input().split(" "))
cards_list, cards_dict = [],{}
index = 0
for _ in range(cards):

    card = input()
    cards_list.append(card)
    cards_dict[card] = index
    index += 1

count  = 0
visited = []
visited_dict = {}
for a_pos in range(0,len(cards_list)):

    for b_pos in range(a_pos+1,len(cards_list)):
        new = str(a_pos)+" "+str(b_pos)
        if new not in visited_dict:
            diff = calc_diff(cards_list[a_pos],cards_list[b_pos])

            if diff in cards_dict:
                loc = cards_dict[diff]
                if loc > a_pos and loc > b_pos:
                    perm = combinations((a_pos,b_pos,diff),2)
                    for i in perm:
                        visited_dict[str(i[0])+" "+str(i[1])] = "visited"
                    count += 1

print(count)