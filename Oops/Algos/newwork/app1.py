#Lists
#ordered, mutable , allows duplicate elements
mylist = [10,'welcome','hello',23.5]
type(mylist)

mylist2 = ['welcome', 'hello','hi','winter','summer']
type(mylist2)

for i in mylist:
    print(i)

for i in mylist:
    if isinstance(i,int):
        print(i)
    else:
        print('element is not int', 'and', type(i))

for i in mylist:
    if isinstance(i,str):
        print(i)
    else:
        print('element is an int')

mylist3 =  []
type(mylist3)

mylist4 = list()
type(mylist4)

mylist4.clear()
for i in mylist:    
    if isinstance(i,str):
        mylist4.append(i)
        print(mylist4)
    else:
        print('element is an int')

mylist
mylist2
mylist3
mylist4

mylist2
mylist2.sort(reverse=False)
print(mylist2)

mylist2.count('welcome')

mylist2.clear()
mylist2
mylist2 = ['welcome', 'hello','hi','winter','summer']
for i in mylist2:
    if mylist2.index(i) < len(mylist2):
        print(i)

for  i in mylist2:
    if i[0] == 'w':
        print(i)

mylist5 = ['hi this is you','hello is this you', 'this can be you','me and you']

for i in mylist5:
    print(i,type(i))

for i in mylist5:
    if i.split(" ").count('you') == 1:
        print(i,i.index('you'))

def kvalue(x):
    y = x.split(" ")
    return y[0],y

for i in mylist5:
    kvalue(i)

for i in mylist5:
    kvalue(i)[0]

for i in mylist5:
    type(kvalue(i))

for i in mylist5:
    type(kvalue(i)[1])

for i in mylist5:
    type(kvalue(i)[0])


lst = []
def readf():
    with open("D:\\GitContent\\Datasets\\Datasets_For_Work\\txt_sentoken\\neg\\cv000_29416.txt",'r') as f:
        content = f.readlines()
        for i in content:
            lst.append(i)
            print(i,end="||")

#append to add element towards end

mylist6 = ['hi this is you','hello is this you', 'this can be you','me and you']

mylist6.append('cool!!!!')

mylist6

#insert at a particular position
mylist6.insert(1,'hello')

mylist6

mylist6.remove('hello')

mylist6

mylist6.remove('cool!!!!')

mylist6

mylist6.pop()

mylist6

#in place
mylist6.sort()
mylist6

#new  list sorted
mylist7 = sorted(mylist6,reverse=True)
mylist7

mylist6.reverse()
mylist6
mylist6.reverse()
mylist6

mylist8 = [1,2,3]
mylist9 = [4,5,6]

newlst = mylist8 + mylist9

newlst

#slicing
