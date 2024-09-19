import random
class Store:
    """
    Appl to insert,remove elements or even find a random element
    Args:
        value (int): The number to be inserted
    Returns:
        map : of elements added
    """
    def __init__(self):
        """
        Display function
        """
        self.map = set()
        Store.disply(self)
    def disply(self):
        """
        xxx function
        """
        print(self.map)
    def insert(self,value):
        """
        Display function
        """
        self.map.add(value)
    def remove(self,value):
        """
        Display function
        """
        self.map.remove(value)
    def getrandmvalue(self):
        """
        Display function
        """
        print(random.choice(list(self.map)))

def main():
    """
    Testing run
    """
t1 = Store()
t1.insert(10)
t1.insert(20)
t1.disply()
t1.remove(10)
t1.disply()
if __name__ == '__main__':
    main()
