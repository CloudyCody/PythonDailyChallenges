# QUESTION:
# This is an interview question asked by Google.
# Given a list of integers S and a target number k, write a function that returns a subset of S 
# that adds up to k. If such a subset cannot be made, then return null. Integers can appear more
# than once in the list. You may assume all numbers in the list are positive.
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

# 1:
def sum_set(s,k): 
    base = []   
    lst = [base] 
    for i in range(len(s)): 
        orig = lst[:] 
        new = s[i] 
        for j in range(len(lst)): 
            lst[j] = lst[j] + [new] 
        lst += orig
    answer=[]
    for r in lst:
        if sum(r)==k:
            answer=r
    return answer

# 2:
from itertools import permutations
def subset(lst, k):
    for i in range(1, len(lst)+1):
        x = [j for j in permutations(lst, i)]
        for p in x:
            if sum(p) == k:
                return p

# 3:
def subarraySum(nums,k):
    result = []
    for i in nums:
        result += [j + [i] for j in result]
        result.append([i])
    return list(filter(lambda x: sum(x) == k, result))