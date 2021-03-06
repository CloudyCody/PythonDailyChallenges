# QUESTION: Level of Interview Question = Easy
# Write an algorithm to determine if a number n is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the number
# equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers
# for which this process ends in 1 are happy numbers.
# Return True if n is a happy number, and False if not. (edited) 

# çözüm:1
def happy(n):
    answer=[]
    while n!=1:
        summ=0
        for i in str(n):
            summ+=int(i)**2
        if summ in answer: 
            return False
        else:
            answer.append(summ)
        n=summ
    return True

# çözüm:2
def isHappy(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum(int(i)**2 for i in str(n))        
    return True if n == 1 else False