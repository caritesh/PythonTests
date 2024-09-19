def lsearch(list,target):
    """
    finds a target from a list by linearly looking for every element
    O(n) as time complexity
    """

    if len(list) == 0:
        print('no elements to search from')
        return
    elif list[0] == target:
        print('element found @', 0)
    elif list[len(list)-1] == target:
        print('ement found @', len(list)-1)
    else:
        for i in range(1,len(list)):
            if i == target:
                print('element found at ', list.index(i))
                return list.index(i)
    print('element nt found')
    return None
        