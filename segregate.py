# QUESTION:
# This is an interview question asked by Google.
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the
# array so that all the Rs come first, the Gs come second, and the Bs come last. You can only
# swap elements of the array.
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become
# ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def transform1(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr