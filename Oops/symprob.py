""" def symmetric_difference_two_sets(set_a, set_b):
    # Symmetric difference between two sets can be 
    # obtained using the ^ operator in Python
    return set_a ^ set_b

def sym(*args):
    # Convert the list of lists into a list of sets
    sets = [set(arg) for arg in args]
    
    # Use the functools.reduce function to apply symmetric_difference_two_sets to all sets
    from functools import reduce
    sym_diff_set = reduce(symmetric_difference_two_sets, sets)
    
    # Convert the set back to a list before returning
    return list(sym_diff_set)


sym([1, 2, 3,3], [5, 6,2, 1, 4], [2, 1])
"""

""" 
x = [(1,10),(2,4),(8,10),(9,10)]

#for i in x:
#    print(i,type(i))

y = []   
def func1(x):
    for i in x:
       y.append(range(i[0],i[1]))
func1(x)

for i in y:
    for j in y:
        print(i,j)

counter = 0
for i in y:
    for j in y:
        if set(i) <= set(j) and set(i) != set(j):
            counter += 1
            print('found match', 'i is ', i, 'j is ', j)
print(counter)

"""
#y = [(1,10),(2,4),(8,10),(9,10)]




