'''
https://leetcode.com/problems/palindrome-number/
'''

x = int(input())


print(True if str(x) == str(x)[::-1] else False)