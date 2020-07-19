#Navigating the web tree using various techniques

#get the required library
from bs4 import BeautifulSoup

#create html document
book_html_doc = """
<catalog><books>
<book id ="bk001">
<author>Hightower, Kim</author>
<title>The First Book</title>
    <genre>Fiction</genre>
    <price>44.95</price>
    <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
</book>
<book id ="bk002">
<author>Nagata, Suanne</author>
<title>Becoming Somebody</title>
    <genre>Biography</genre>
    <review>A masterpiece of the fine art of gossiping.</review>
</book>
<book id ="bk003">
<author>Oberg, Bruce</author>
<title>The Poet's First Poem</title>
    <genre>Poem</genre>
    <price>24.95</price>
    <review>The least poetic poems of decade.</review>
</book>
</books>
</catalog>"""

#create a soup object and pass web document as a paramter
book_soup = BeautifulSoup(book_html_doc,'html.parser')

#print the catalog tag
print(book_soup.catalog)

#view the head of the book html doc (here we have various tags such as head, title, bold etc)
book_Soup.head

#view the title of the book html doc
title_tag = book_soup.title
title_tag

#print the catalog bold tag
print(book_soup.catalog.p)

#navigate down the descendants and print them
for descen in book_soup.head.descendants:
    print(descen)

#Its possible to navigate down a tree, using descendants or the stripped string method
#navigate down using stripped string method
for string in book_soup.stripped_strings:
    print(repr(string))

#navigate up using parent method
title_tag.parent

#create element object to navigate back and forth
element_soup = book_soup.catalog.books

#navigate forward using next_element method (1st next element takes to new line and next one takes to actual string value)
next_element =  element_soup.next_element.next_element
next_element

#navigate back using previous_element method
previous_element = next_element.previous_element.previous_element
previous_element

#navigating sideways
#create a sibling object and navigate to view it
next_sibling = book_soup.catalog.books.book
next_sibling

#navigate to next sibling
next_sibling2 = next_sibling.next_sibling
next_sibling2.next_sibling

#navigate to previous sibling
previous_sibling = next_sibling2.previous_sibling
previous_sibling