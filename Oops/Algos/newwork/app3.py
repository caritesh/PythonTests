def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    --This has 3 main steps
    Divide : Find the midpoint of the list nd divide into sublists
    Conquer: Recursively sort the sublists created in previous steps
    Combine: Merge the sorted sublists created in previous step
    Runs : O(k*n log n) time
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    O(k log n) --since slicing 
    
    """
    midpoint = len(list)//2
    left = list[:midpoint]
    right = list[midpoint:]
    return left,right

def merge(left,right):
    """
    merges two lists(arrays), sorting them in process
    Returns a new merged list
    Runs O(n)
    """
    l = []
    i = 0 #i for indexes in left list
    j = 0 #j for indexes in right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1 

    while i < len(left) :
        l.append(left[i])
        i += 1
    
    while j < len(right) :
        l.append(right[j])
        j += 1
    
    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[2:])

