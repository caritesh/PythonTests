import random
values = []
mymap = {}
type(values)
type(mymap)

def tesf(x):
    if x not in values:
        values.append(x)
        mymap[x] = len(values)-1
    print(values, mymap)

def remf(x):
    if x not in mymap:
        return
    index = mymap[x]
    #swapping
    last_val = values[-1]
    values[-1] = x
    values[index] = last_val
    mymap[last_val] = index
    values.pop()
    del mymap[x]

def get_random():
    return random.choice(values)

 