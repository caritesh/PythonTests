
""" import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')
print(stopwords.words('english'))
print(stopwords.words('german'))
print(stopwords.words('french'))
print(stopwords.words('arabic')) 
"""
#Linear Search
""" def linear_search(list,target):
    #Docustring-Returns the index position of the target if found, else returns None
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None


#Binary Search
def binary_search(list,target):
    first = 0
    last = len(list) -1
    while first <= last:
        midpoint = first+last//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("target found at index   ", index)
    else:
        print("Target not found in list")
"""
""" def recur_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recur_binary_search(list[midpoint+1:], target)
            else:
                return recur_binary_search(list[:midpoint],target)

def verify(result):
    print("Target not found in list", result)

#Note for binary_search the passed on list should be sorted
#Time notation: O(logn) < because of while loop

numbers = [1,2,3,4,5,6,7,8,9,10]
result = recur_binary_search(numbers, 2)
verify(result)

"""
#Python prefers iteration instead of recursive solution as 
#python has a limit on max recursion

# https://www.youtube.com/watch?v=8hly31xKli0

""" 
class Node:
    """An object fr storing a single node of a linked list
        Models two attr - data and the link to the next node in the list
        """
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
    
    def __repr__(self):
        return "data is: %s" % self.data
        
class LinkedList:
    """singly linked list"""

    def __init__(self):
        self.head = None
        # Maintaining a count attribute allows for len() to be implemented in
        # constant time
        self.__count = 0
    
    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        """
        Returns the length of the linked list
        Takesn O(1) time
        """

        return self.__count

    #convenience method
    def size(self):
        """returns the num of nodes in the list and takes linear time O(n)"""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self,data):
        """add new Node containing data at head of the list, takes O(1)"""
        new_head = Node(data,next_node=self.head)
        self.head = new_head
        self.__count += 1
    
    def search(self, key):
        """Search for the first node cntaining data that matches the key
            Return the node or 'None' if not found
            Takes O(n) time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
        
    def insert(self, data, index):
        """insert a new node containing data at index position
        inserttion takes o(1), finding node at insertion place takesn o(n)
        therefore overall o(n) i.e. linear time
        """
        if index >= self.__count:
            raise IndexError('index out of range')
        
        if index == 0:
            self.add(data)
            return
        
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                #print('current now is: ', current)
                current = current.next_node
                #print('current now is: ', current)
                position -= 1
            
            prev_node = current
            next_node = current.next_node
            prev_node.next_node = new
            new.next_node = next_node

        self.__count += 1

    def node_at_index(self, index):
        """
        Returns the Node at specified index
        Takes O(n) time
        """

        if index >= self.__count:
            raise IndexError('index out of range')

        if index == 0:
            return self.head

        current = self.head
        position = 0

        while position < index:
            current = current.next_node
            position += 1

        return current

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or `None` if key doesn't exist
        Takes O(n) time
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
                self.__count -= 1
                return current
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
                self.__count -= 1
                return current
            else:
                previous = current
                current = current.next_node

        return None

    def remove_at_index(self, index):
        """
        Removes Node at specified index
        Takes O(n) time
        """

        if index >= self.__count:
            raise IndexError('index out of range')

        current = self.head

        if index == 0:
            self.head = current.next_node
            self.__count -= 1
            return current

        position = index

        while position > 1:
            current = current.next_node
            position -= 1

        prev_node = current
        current = current.next_node
        next_node = current.next_node

        prev_node.next_node = next_node
        self.__count -= 1

        return current


    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next_node
        
    def __repr__(self):
        """Return a string repr of the list, takes O(n) time"""

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head:  %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail:  %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)            
            current = current.next_node
        return '-> '.join(nodes) 

l = LinkedList()
l1 = Node(10)
l.head = l1
l.size() 



l = LinkedList()
l.add(1)
l.size()
l.add(2)
l.size()
l
l.search(2)
"""





    











