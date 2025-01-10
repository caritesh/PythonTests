#static method
"""class Math:
    def __init__(self):
        pass

    @staticmethod
    def add5(x):
        return x+5

print(Math.add5(10))"""

#prnt with options
"""
print('hello','world', end = ',',sep = '|' )

help(print)
"""
#help function
"""
    def myfunc(x,y):
    #this function can add two numbers
    #x: value1
    #y: value2
    #returns sum of x and y : int
    return x+y
"""

"""
help(myfunc)
"""

#range function
"""
rng = range(10)
type(rng)
print(rng)
print(list(rng))

rng2 = range(2,10)
rng3 = range(2,10,2)
"""

#wrking with strings
"""
strings = ['hello','welcome','winter','summer']
frstletter_n_word = list(map(lambda n: (n[0],n),strings))
frstletter_n_word

from itertools import groupby
grouped_strngs = groupby(strings, lambda n: n[0])
for k,g in grouped_strngs:
    print(k,list(g))

mapped_data = map(lambda n: (len(n),n),strings)
print(list(mapped_data))
filtered_data = filter(lambda n: len(n)>=7,strings)
print(list(filtered_data))

lst = [['hi this is me'],['hi this is me'],['no this is not me']]
for i in lst:
    print(i, type(i))

def functest(*args):
    for i in args:
        print(args.index(i))

functest(lst)     
"""

#wrking with list of strings
"""
lst = ['this is a new book','this is a new table']
type(lst)
lst2 = []

for i in lst:
    lst2.append(i.split(" "))

lst2

for i in lst2:
    for j in i:
        print(j,lst2.index(i))
"""

#sorting
"""
strings
sorted(strings)
sorted(strings,reverse=True)

people = [
{"name": "john","age": 30},
{"name": "peter","age": 35}
]

sortedlst = sorted(people, key = lambda n : n["age"])
sortedlst
sortedlst = sorted(people, key = lambda n : n["age"],reverse = True)
sortedlst
"""
#using enumerate
tasks = ['Write report','Attend meeting','Review code']
for index in range(len(tasks)):
    task = tasks[index]
    print(f"{index +1}. {task}")

for index,task in enumerate(tasks):
     print(f"{index+1}. {task}, {index}")
print(list(enumerate(tasks)))

#zip function
names = ['john','mary','alice']
ages = [10,20,30]
for indx in range(min(len(names),len(ages))):
     name = names[indx]
     age = ages[indx]
     print(f"{name} is {age} yrs old")

#using zip
names = ['john','mary','alice']
ages = [10,20,30]
combined = list(zip(names,ages))
combined
for name,age in combined:
     print(f"{name} is {age} yrs old")

file = "D:\\GitContent\\Datasets\\Datasets_For_Work\\test.csv"

fileopn = open(file,"w")
fileopn.write("testing writing hello world\ntesting again")
fileopn.close()

#append
with open("D:\\GitContent\\Datasets\\Datasets_For_Work\\test.csv","a") as file:
     file.write("\ntesting third time")

#read
with open("D:\\GitContent\\Datasets\\Datasets_For_Work\\test.csv","r") as file:
     text = file.read()
     print(text)


    





    

