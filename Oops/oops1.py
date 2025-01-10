""" 
class Item:
    def calculate_total_price(self,x,y):
        return x * y

item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5

item2 = Item()
item2.name = 'SmartPhone'
item2.price = 200
item2.quantity = 15

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

print(item1.calculate_total_price(item1.price,item1.quantity))
print(item2.calculate_total_price(item2.price,item2.quantity))

"""
""" 
class Item:
    def __init__(self, name, price, quantity):
        print(f'An instance created > {name}')
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self,x,y):
        return x * y

item1 = Item('Phone',100,5)
item2 = Item('SmartPhone',1000,3)

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item2.name)
print(item2.price)
print(item2.quantity)
"""

""" 
import csv
class Item:
    pay_rate = 0.8 #payrate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity= 0):
        #run validations on received argument values
        assert price >= 0, f"Price {price} is not greater or eq to 0!"
        assert quantity >= 0 , f"Price {quantity} is not greater or eq to 0!"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('C:\\Users\\Ajay\\Downloads\\PythonTests\\Algos\\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item  in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )        

    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"


#item1 = Item('phone',100,5)
#item2 = Item('SmartPhone',1000,3)
#item3 = Item('laptop',1000)
#print(f'name: {item3.name} \nprice: {item3.price} \nquantity: {item3.quantity}')
#item2.has_numpad = False
#print(item1.calculate_total_price())
#print(item2.calculate_total_price())

#assigning negative values and checking validation
#item1 = Item('phone',100,-5)
#print(item1.calculate_total_price())

#print(Item.pay_rate)
#print(item1.pay_rate)
#print(item2.pay_rate)

#print(Item.__dict__) #shows all attributes for class
#print(item1.__dict__)

#for i in Item.__dict__.keys():
#    print(i)

#item1.apply_discount()
#print(item1.price)

#item2 = Item('SmartPhone',1000,3)
#item2.pay_rate = 0.7
#print(item2.price)
#item2.apply_discount()
#print(item2.price)

#print(Item.all)

#for i in Item.all:
#    print(i.name)

#Item.instantiate_from_csv()

#Item.instantiate_from_csv()
#for i in Item.all:
#    print(i)
"""
""" 
class Item:
    pay_rate = 0.8 #the pay rate after 20% discount
    def __init__(self,name: str, price: float, quantity=0):
        #using assert statements to do the validations
        #also include our own exception statements
        assert price >= 0, f"Price {price} is not greater than or eq to 0"
        assert quantity >=0 , f"Quantity {quantity} is not greater than or  eq to 0"
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        #self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

print(Item.pay_rate)

item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 200, 3)
print(item1.pay_rate)

#print(item1.calculate_total_price())
#print(item2.calculate_total_price())

#accessing using internal special methods
print(Item.__dict__) #to see all attr at the class level
print(item1.__dict__) #to see all attr at the instance level

print(item1.price)
item1.apply_discount()
print(item1.price)
#item1.apply_discount()
#print(item1.price)

#assigning a specific disct to specific instance
#here this attr would be found at instance level and thus overrides prev defined at class
#we need to make sure that method contains 'self.pay_rate' instead of 'Item.pay_rate'
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

#if no pay_rate defined at instance level, then attr at class lvl is considered
item3 = Item('Laptop-screen', 1000, 5)
item3.apply_discount()
print(item3.price) #20% discount
"""

""" 
class Item:
    pay_rate = 0.8 #the pay rate after 20% discount
    all = []
    def __init__(self,name: str, price: float, quantity=0):
        #using assert statements to do the validations
        #also include our own exception statements
        assert price >= 0, f"Price {price} is not greater than or eq to 0"
        assert quantity >=0 , f"Quantity {quantity} is not greater than or  eq to 0"
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
        #actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        #self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

    #using representative presentation
    def __repr__(self) -> str:
        return f"Item('{self.name}',{self.price},{self.quantity})"
    
item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 200, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('keyboard', 75, 5)

print(Item.all)

for i in Item.all:
    print(i.name,i.price,i.quantity)

"""
""" 
import csv
class Item:
    pay_rate = 0.8 #the pay rate after 20% discount
    all = []
    def __init__(self,name: str, price: float, quantity=0):
        #using assert statements to do the validations
        #also include our own exception statements
        assert price >= 0, f"Price {price} is not greater than or eq to 0"
        assert quantity >=0 , f"Quantity {quantity} is not greater than or  eq to 0"
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
        #actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        #self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

    @classmethod #class reference is passed as frst argument
    def instantiate_from_csv(cls):
        with open('Algos\\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
            #for item in items:
            #print(item)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )
     
    #using representative presentation
    def __repr__(self) -> str:
        return f"Item('{self.name}',{self.price},{self.quantity})"
    
Item.instantiate_from_csv()
print(Item.all)

"""
#wrking with static method
""" 
import csv
class Item:
    pay_rate = 0.8 #the pay rate after 20% discount
    all = []
    def __init__(self,name: str, price: float, quantity=0):
        #using assert statements to do the validations
        #also include our own exception statements
        assert price >= 0, f"Price {price} is not greater than or eq to 0"
        assert quantity >=0 , f"Quantity {quantity} is not greater than or  eq to 0"
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
        #actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        #self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

    @classmethod #class reference is passed as frst argument
    def instantiate_from_csv(cls):
        with open('Algos\\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
            #for item in items:
            #print(item)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod #instance is not sent as frst argument
    def is_integer(num):
        #we will count out floats that are point zero ex: 5.0,10.0 etc
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    #using representative presentation
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
    
#Item.instantiate_from_csv()
#print(Item.all)

print(Item.is_integer(5))
print(Item.is_integer(7.0))
print(Item.is_integer(7.5))

#static mthod when smthing to be done is not unique to the instance
#manipulate different structures of data to instantiate objects
#we can call both staticmethod & classmethod from instance of an object.

"""
import csv
class Item:
    pay_rate = 0.8 #the pay rate after 20% discount
    all = []
    def __init__(self,name: str, price: float, quantity=0):
        #using assert statements to do the validations
        #also include our own exception statements
        assert price >= 0, f"Price {price} is not greater than or eq to 0"
        assert quantity >=0 , f"Quantity {quantity} is not greater than or  eq to 0"
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
        #actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        #self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

    @classmethod #class reference is passed as frst argument
    def instantiate_from_csv(cls):
        with open('Algos\\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
            #for item in items:
            #print(item)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod #instance is not sent as frst argument
    def is_integer(num):
        #we will count out floats that are point zero ex: 5.0,10.0 etc
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    #using representative presentation
    #def __repr__(self):
    #    return f"Item('{self.name}',{self.price},{self.quantity})"
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

#to work and solve on issue with one item such as phone and modify its price if brokn
#phone1 = Item("jscPhonev10",500,5)
#phone1.broken_phones = 1
#phone2 = Item("jscPhonev20",700,5)
#phone2.broken_phones = 1

class Phone(Item):
    #all = []
    def __init__(self,name: str, price: float, quantity=0, broken_phones=0):
        #call to super fnc
        super().__init__(name,price,quantity)
        #using assert statements to do the validations
        #also include our own exception statements
        assert price >= 0, f"Price {price} is not greater than or eq to 0"
        assert quantity >=0 , f"Quantity {quantity} is not greater than or  eq to 0"
        assert broken_phones >=0 , f"Quantity {broken_phones} is not greater than or  eq to 0"
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones

        #Phone.all.append(self)

#since inheritance
#phone1 = Phone("jscPhonev10",500,5,1)
#phone2 = Phone("jscPhonev20",700,5,2)
#print(Item.all)
#print(Phone.all)










        































