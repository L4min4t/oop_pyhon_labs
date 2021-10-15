from Customer import Customer
from Product import Product

class Order:
    """
    holds order info
    """
    id_generator = 0
    def __init__(self, customer, *products):
        self.customer = customer
        self.products = list(products)
        self.total_order_value
        self.id = Order.id_generator
        Order.id_generator += 1

    def add_item(self, item):
        if not isinstance(item, Product):
                raise TypeError("products must be Product type")
        if item.quantity == 0:
                raise ValueError(f'no goods (id {item.id}) in stock')
        item.quantity -= 1
        self.__products.append(item)
    
    def del_item(self, item):
        if not isinstance(item, Product):
                raise TypeError("products must be Product type")
        item.quantity += 1
        self.__products.remove(item)

    @property
    def total_order_value(self):
        return self.count_total_order_value()

    def count_total_order_value(self):
        total_order_value = 0
        for i in self.products:
           total_order_value += i.price
        return total_order_value
        

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID must be int")
        if value < Order.id_generator:
            raise ValueError("ID generation failure")
        self.__id = value
    
    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        for i in products: 
            if not isinstance(i, Product):
                raise TypeError("products must be Product type")
        self.__products = products
        for item in self.__products:
            if item.quantity == 0:
                raise ValueError(f'no goods (id {item.id}) in stock')
            item.quantity -= 1

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be Customer type")
        self.__customer = customer

    def __str__(self) -> str:
        order_info = f'ID order: {self.id}\n<-------->\n{self.customer}\n<-------->\nTotal price: {self.total_order_value} UAH\n<-------->\nItems:\n'
        for item in self.products:
            order_info = order_info + item.info_for_order() + '\n' + '--------' + '\n'
        return order_info[0:-1]