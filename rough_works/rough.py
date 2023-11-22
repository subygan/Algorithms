
def longestPalindrome(s: str) -> str:

    R = 0
    max_R = 0
    max_palindrome = ""
    s = s.replace("","#")
    print(s)

    if len(s) <= 3:
        return s.replace("#","")

    for i in range(0,len(s)):
        # print("-------")
        R = 0
        # print(s[i])
        while i+R<=len(s)-1 and i-R>0 and s[i+R-1] == s[i-R-1]:
            # print("<<=====>>")
            # print(s[i-R-1],s[i+R-1])
            # print(R,s[i-R-1:i+R])
            if max_R<=R:
                print("^",R)
                max_R = R
                max_palindrome = s[i-R-1:i+R].replace("#","")
            R+=1
    print(max_palindrome)
    return max_palindrome

if __name__ == '__main__':
    longestPalindrome("babad")