#for loop example
words = ['hello','cool','test','why']
for w in words:
    if w == 'hello':
        print('word found')
    else:
        print('word not same as presented')
print('*'*10)
#
for w in words:
    if w[0] in ('a','e','i','o','u'):
        print('first letter is a vowel')
    else:
        print('vowel not found as frst letter of word')

#
x = range(0,10)
for n in x:
    if n<=6:
        print(n)
    else:
        print('stop!')
        break

#
x = range(101,110,2)
for n in x:
    if( n > 103):
        print(n)
    else:
        print("n is not bigger than 100 so ignoring it")