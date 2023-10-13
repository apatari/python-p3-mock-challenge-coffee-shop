class Coffee:

    all = []

    def __init__(self, name):
        self.name = name
        Coffee.add_coffee_to_all(self)

    @classmethod
    def add_coffee_to_all(cls, coffee):
        cls.all.append(coffee)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        if isinstance(val, str) and len(val) >=3 and not hasattr(self, 'name'):
            self._name = val
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        cust_list = ([order.customer for order in Order.all if order.coffee == self])
        seen = set()
        res = []
        for cust in cust_list:
            if cust not in seen:
                seen.add(cust)
                res.append(cust)
        return res

    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        total_price = 0
        for order in self.orders():
            total_price += order.price

        return total_price / self.num_orders()

class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.add_customer_to_all(self)

    @classmethod
    def add_customer_to_all(cls, cust):
        cls.all.append(cust)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if isinstance(val, str) and len(val) and len(val) < 16:
            self._name = val
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        seen = set()
        res = []
        coffee_list = [order.coffee for order in self.orders()]
        for coffee in coffee_list:
            if coffee not in seen:
                seen.add(coffee)
                res.append(coffee)
        return res

    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        res = None
        current_total = 0
        for customer in cls.all:
            all_prices = [order.price for order in customer.orders() if order.coffee == coffee]
            if all_prices:
                total = sum(all_prices)
                if not res or total > current_total:
                    res = customer
                    current_total = total
        return res


    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.add_order_to_all(self)

    @classmethod
    def add_order_to_all(cls, order):
        cls.all.append(order)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, val):
        if isinstance(val, float) and 1 <= val <= 10 and not hasattr(self, 'price'):
            self._price = val

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, val):
        if isinstance(val, Customer):
            self._customer = val
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, val):
        if isinstance(val, Coffee):
            self._coffee = val
