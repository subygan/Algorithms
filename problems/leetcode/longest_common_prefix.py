'''
https://leetcode.com/problems/longest-common-prefix/submissions/
'''
def longestCommonPrefix( strs) -> str:
    if strs:
        mine = strs[0]
    else:
        mine = ''

    for word in strs:
        new = ''
        if mine:
            for letter in range(len(word)):
                try:
                    if mine[letter] == word[letter]:
                        new += mine[letter]
                    else:
                        break
                except IndexError:
                    break
            mine = new
        else:
            break
    return mine
