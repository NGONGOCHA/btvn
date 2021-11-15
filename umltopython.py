class Payment:
    def __init__(self, amount:float):
        self.amount = amount

class Cash(Payment):
    def __init__(self, amount:float, cashTendered:float):
        super().__init__(amount)
        self.cashTendered = cashTendered

class Check(Payment):
    def __init__(self, amount:float, name:str, bankID:str):
        super().__init__(amount)
        self.name = name
        self.bankID = bankID

    def authorized():
        pass

class Credit(Payment):
    def __init__(self, amount:float, number:str, type:str, expDate):
        super().__init__(amount)
        self.number = number
        self.type = type
        self.expDate = expDate
    
    def authorized():
        pass

class Item:
    def __init__(self, shippingWeight, description:str):
        self.shippingWeight = shippingWeight
        self.description = description

    def getPriceForQuantity():
        pass

    def getTax():
        pass

    def inStock():
        pass

class OrderDetail(Item):
    def __init__(self, shipping, description:str, quantity, taxStatus:str):
        super().__init__(shipping, description)
        self.quantity = quantity
        self.taxStatus = taxStatus

    def calcSubTotal():
        pass

    def calcWeight():
        pass

    def calcTax():
        pass

class Order:
    def __init__(self, date, status:str):
        self.date = date
        self.status = status

    def calcSubTotal():
        pass

    def calcTax():
        pass

    def calcTotal():
        pass

    def calcTotalWeight():
        pass

class Customer:
    def __init__(self, name:str, address):
        self.name = name
        self.address = address