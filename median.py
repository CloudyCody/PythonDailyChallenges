# QUESTION:
# This is an interview question asked by Microsoft.
# Compute the running median of a sequence of numbers. That is, given a stream of numbers,
# print out the median of the list so far on each new element. Recall that the median of an
# even-numbered list is the average of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

# çözüm 1:
lst = []
items = [2, 1, 5, 7, 2, 0, 5]
for i in items:
    lst.append(i)
    half = len(lst) // 2
    lst.sort()
    if not len(lst) % 2:
        print((lst[half - 1] + lst[half]) / 2.0)
    else:
        print(lst[half]) 
    
# çözüm2:

def median(lst):
    lst.sort()
    mid = len(lst) // 2
    return lst[mid] if len(lst) % 2 != 0 else (lst[mid] + lst[mid-1]) / 2 
lst = [2, 1, 5, 7, 2, 0, 5]
for i in range(1,len(lst)):
    print(median(lst[:i]))