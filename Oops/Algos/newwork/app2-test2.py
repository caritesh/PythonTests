#Binary search
def bsearch(lst,target):
    
    if len(lst) == 0:
        print('no elements in lst')
        return
    
    first = 0
    last =  len(lst)-1
    
    if lst[first] == target:
        print('target found @: ', 0)
        
    elif lst[last] == target:
        print('target found @: ', len(lst)-1)

    else:
        mid = first+last//2
        if lst[mid] == target:
            print('target found at mid:', mid)
        elif lst[mid] < target:
            first = mid + 1
            print('target found xx-')
        else:
            last = mid - 1
            print('target found xy-')
    return None
