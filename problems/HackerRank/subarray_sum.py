def findSum(numbers, queries):
    # Write your code here
    for query in queries:
        total = sum( [i if i>0 else query[2] for i in numbers[query[0]:query[1]]])