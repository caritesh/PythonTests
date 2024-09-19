bkttls = ['book1','book2','book3','book4','book5']
bkconts = ['this is a new math book',
           'this is a new math book',
           'this is a science book',
           'science book is good',
           'this isnt a new math book']
mybooks = dict(zip(bkttls,bkconts))
type(mybooks)
for i in mybooks:
    print(i,mybooks[i])
import nltk 
import nltk.corpus
import stopwords
stop_words = stopwords.get_stopwords('english')

def remove_sw(sentence):
    words = sentence.split(" ")
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

for i in mybooks.keys():
    print(i,remove_sw(mybooks[i]))

mybooks

for i in mybooks.keys():
    mybooks[i] = remove_sw(mybooks[i])

for i in mybooks:
    print(i,mybooks[i])

#lst = list()
#for i in mybooks.keys():
#    lst.append(mybooks[i])

x = map(lambda n: (n.split(" ")),mybooks.values())

for i in x:
    for j in x:
        if i==j and i[0] in j:
            print(i,j)

y = list(map(lambda n: (n.split(" ")),mybooks.values()))
for i in y:
    for j in y:
        print(i,j)



