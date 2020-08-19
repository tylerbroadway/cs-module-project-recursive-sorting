# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a = 0
    b = 0
    c = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a += 1
        else:
            merged_arr[c] = arrB[b]
            b += 1
        c += 1

    while a < len(arrA):
        merged_arr[c] = arrA[a]
        c += 1
        a += 1

    while b < len(arrB):
        merged_arr[c] = arrB[b]
        c += 1
        b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        end = len(arr)
        start = 0
        mid = (start + end) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here

def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

# Quick Sort
# def partition(arr):
#     # choose pivot
#     pivot = arr[0]
#     left = []
#     right = []
#     # partition around the pivot
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         else:
#             right.append(num)

#     return (left, pivot, right)

# def quick_sort(arr):
#     # Base Case: empty array
#     if len(arr) == 0:
#         return arr
    
#     # recurse on left and right sides
#     left, pivot, right = partition(arr)
    
#     return quick_sort(left) + [pivot] + quick_sort(right)

# print(quick_sort([1, 3, 11, 4, 6, 5, 9]))
