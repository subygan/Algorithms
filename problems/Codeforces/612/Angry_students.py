'''
https://codeforces.com/contest/1287/problem/A
Note :
Was trying to solve this problems in a brute force method, by implementing the same
Algorithm in the question.
When in reality there was a much simpler and easy algorithm.
'''
if __name__ == "__main__":

    test_cases = int(input())
    for _ in range(test_cases):
        student_no = int(input())
        split_value = input().split("A")

        if len(split_value)<2:
            print(0)
        else:
            print(len(max(split_value[1:])))