import random
class newcls:
    mynums = set()
    def __init__(self,numvalue):
        self.numvalue = numvalue
        if self.numvalue in newcls.mynums:
                print('number already exists,so set remains same')
        else:
            newcls.mynums.add(self.numvalue)
        newcls.disply()
    
    def disply():
        print(newcls.mynums)
    
    @classmethod
    def remele(cls,value):
        cls.mynums.remove(value)
        print(newcls.mynums)
    
    @classmethod
    def randomValue(cls):
         print(random.sample(cls.mynums,1))

def main():
     t1 = newcls(10)
     t2 = newcls(100)
     t3 = newcls(1000)
     t4 = newcls(1000)
     t4 = newcls.remele(10)
     t5 = newcls.randomValue()

if __name__ == '__main__':
   main()

