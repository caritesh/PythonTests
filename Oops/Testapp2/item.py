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
        self.__name = name
        #self.name = name
        self.__price = price
        self.quantity = quantity
    
        #actions to execute
        Item.all.append(self)

    #working with read only attrs (using decorators)
    """@property
    def read_only_name(self):
        return "AAA" """

    @property
    #Property Decorator = Read-only attribute
    def name(self):
       return self.__name
    
    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise Exception("value too long")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def calculate_total_price(self):
        return self.__price * self.quantity
    
    def apply_discount(self):
        #self.price = self.price * Item.pay_rate
        self.__price = self.__price * self.pay_rate

    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price * increment_value

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
        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"


    

