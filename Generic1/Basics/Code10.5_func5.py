def mysum(n):
    return n * 1000

mylist = [23,34,45,56,67]
newlist = []

for i in mylist:
    newlist.append(mysum(i))

newlist

mylist2 = [23,34,45,56,67]
preflist = list(map(lambda n: n*100,mylist2))
preflist

sellist = list(filter(lambda i: i%2==0,mylist2))
sellist

preflist = list(map(lambda n: mysum(n),mylist2))
preflist




