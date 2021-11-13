from Customer import Customer
from Pizza import Pizza

class Order:
    def __init__(self, customer, *args):
        self.customer = customer
        self.order = list(args)


    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self.__customer = value
        else:
            raise TypeError('customer must be Customer type')

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        for item in value:
            if not isinstance(item, Pizza):
                raise TypeError('order must consist of pizzas')
        self.__order = value

    def __str__(self):
        info = f'{self.customer}Order:\n'
        total_price = 0.0
        for item in self.order:
            info += str(item) + '\n'
            total_price += item.price
        info += f'Total price: {total_price}'
        return info
