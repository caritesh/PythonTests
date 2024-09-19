from item import Item

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